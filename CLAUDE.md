# Mezbon

LLM sales agent that sells from a real catalog and takes orders over WhatsApp, and later Telegram. The first
deployment is a bakery. Design and its sources: [architecture doc](https://claude.ai/artifact/7Ey4eyEEFP7tkeg9VkhdH7);
read it before changing the agent loop, tools or order flow.

## Hard rules

These override any task instruction. Code and reviews cite them by number.

1. **Facts come from tools only.** A price, product, size, filling, lead time or free date reaches the customer only
   as a tool result. A test asserts that no reply states a price the turn's tool calls did not return.
2. **Orders are complete or refused.** `create_order` rejects until every required field of the product type is
   filled. The tool enforces this, not the prompt, because a prompt can be talked out of it.
3. **Each tool validates its own input** and returns an error the model can recover from, never an exception that
   ends the turn.
4. **Public repo:** demo catalog and invented conversations only. Real prices, phone numbers, customer messages,
   logs and keys never enter git; secrets come from env vars (`.env`, gitignored).
5. **Verify every webhook** (`X-Hub-Signature-256` for Meta) before parsing it: the endpoint is public.

## Structure

| Path | What |
|---|---|
| `core/` | agent loop, system prompt, guardrails, classifier |
| `tools/` | catalog, cart, date availability, orders, human handoff |
| `channels/<name>/` | one adapter per messenger, mapping its messages to the common message type |
| `domains/<shop>/` | catalog, required fields per product type, persona |

`core/` and `tools/` never import a channel SDK or name a shop: a new messenger is a new adapter, a new shop a new
domain.

## Commands

No code yet: the project skeleton item in `docs/backlog/must-have.md` adds run, test and lint here.

## Conventions

- Python with FastAPI.
- Backlog lives in `docs/backlog/{must-have,should-have,could-have,polish}.md`, one file per tier, created when its
  first item lands; completed items are deleted.

- The agent answers in the customer's language and script; no translation layer, no hardcoded language list.
- Keep replies short: WhatsApp bills each free-form reply past 1,000 per number per month.
- Hand off to a human when the customer is angry, the order falls outside the required fields, or the agent is unsure.
- Behaviour changes ship with scripted customer conversations in `tests/` that run before any deploy.
