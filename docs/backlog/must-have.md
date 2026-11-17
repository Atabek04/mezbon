# Must Have

> What the first bakery deployment cannot go live without, in build order.
>
> `[ ]` not started · `[~]` in progress · `[✓]` implemented
>
> **Completed items are deleted from this file, not archived.** Git history is the record.

---

- [ ] **Bakery product schema** · P0 · M. Product types, their sizes, fillings and lead times, and the required
  order fields per type (a custom cake: date, weight, filling, inscription, pickup or delivery, phone). Everything
  below builds on it.
- [ ] **Demo catalog** · P0 · S. Invented bakery products in `domains/bakery/` that fit the schema; never real prices
  (hard rule 4).
- [ ] **Catalog and cart tools** · P0 · M. `search_products`, `get_product`, `update_cart`, `check_date_available`,
  each validating its own input (hard rule 3).
- [ ] **Order creation** · P0 · M. `create_order` refuses until every required field is filled (hard rule 2), then
  notifies the bakers.
- [ ] **Agent loop** · P0 · L. System prompt with the bakery persona, chat history and current order loaded per turn,
  catalog results injected before each turn, tool calling, replies in the customer's language and script.
- [ ] **WhatsApp adapter** · P0 · M. Cloud API webhook with signature check (hard rule 5), mapping to the common
  message type, sending replies.
- [ ] **Human handoff** · P0 · M. `handoff_to_human` posts the chat to the bakers' Telegram group and stops the agent
  replying in it until a baker hands it back.
- [ ] **Scripted conversation tests** · P0 · M. Invented customer chats in several languages covering a full order,
  a missing field, an off-topic message and a handoff; they gate every deploy.
- [ ] **Meta Business setup** · P0 · S · owner. Meta Business account, WhatsApp Cloud API app and a dedicated phone
  number off the regular WhatsApp app.
