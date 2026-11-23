# Tips & Tricks

[← Back to README](../README.md)

Tips that came from a post or page link to it. Official means an xAI Grok Bot doc or guide. Tips 7 and 47 point to bots on this list.

## On this page

- [Vetting a third-party bot before you add it](#vetting-a-third-party-bot-before-you-add-it)
- [Safety and approval habits](#safety-and-approval-habits)
- [Saving usage](#saving-usage)
- [Writing good routines and skills](#writing-good-routines-and-skills)
- [Useful extras](#useful-extras)
- [Privacy-removal recheck schedules](#privacy-removal-recheck-schedules)

## Vetting a third-party bot before you add it

**1.** Treat templates like software: open View Details and read the context and integrations; make sure everything is exactly what you'd expect before adding. (Official: [Templates guide](https://x.ai/bot/guides/templates-for-grok-bot))

**2.** A template is "a recipe, not a meal": it carries instructions, skills and first-party plugins, not secrets or private info. You still reconnect plugins yourself, and MCP servers/custom code don't come along. (Official: [Templates guide](https://x.ai/bot/guides/templates-for-grok-bot))

**3.** Community templates are not pre-vetted by xAI; review instructions, skills, routines and integrations yourself because prompt-injection risk exists. ([@grok](https://x.com/grok/status/2111495390218371243))

**4.** Quick 3-point check: what it saves to memory, what its routines do and when, and what it asks you to connect. ([@gibsonaihud](https://x.com/gibsonaihud/status/2106437386511245482))

**5.** First message to a new template: "Before any task, list every skill, plugin and integration you came with, what each can access, and anything that can send, pay, post or delete. Ask me before using any of those." ([@NoraHustles](https://x.com/NoraHustles/status/2113991391588364738))

**6.** If a template link won't install, check your Grok Bot and X login are the same account, or ask your bot to build one like it. ([@monetization_x](https://x.com/monetization_x/status/2112031233123520813))

**7.** Use [Bouncer](../categories/security-and-bot-safety.md#bot-o2OyTjWlNOUdYwr61prw_) ([@bradshannon](https://x.com/bradshannon)) or [Template Safety Checker](../categories/security-and-bot-safety.md#bot-8JbRKMaD-VrcN_QyitMXN) ([@Jorhan](https://x.com/Jorhan)) (on this list) to read a template before you add it.

**8.** Template creators can update or retire a shared link. After publishing, the bot's Share menu offers View template details, Update template (pushes your latest changes to the shared copy) and Delete Template (turns the link off). Worth knowing when a bot you shared has a bug, and a reason to re-check a template's page if you added it a while ago. (Official: [Create and manage Bots](https://docs.x.ai/grok-bot/bots))

**9.** Browse templates from inside the app. Open Connect apps in the sidebar and choose Bot templates; the gallery opens on x.ai. On iPhone and Android, share your own bot from its menu with Share as Template. (Official: [Create and manage Bots](https://docs.x.ai/grok-bot/bots))

**10.** Prompt links ask you to confirm before they fill a chat box. Links with suspicious hidden characters are blocked, and card numbers are scrubbed from memories, including in bots shared as templates. (Official: [Grok Bot changelog](https://x.ai/bot/changelog))

## Safety and approval habits

**11.** Put boundaries in the request: say what the bot may do and where it must stop (sending, publishing, purchases, deleting, permissions, accepting terms). (Official: [Approvals, security, and privacy](https://docs.x.ai/grok-bot/approvals-security-and-privacy))

**12.** An approval controls the proposed action; it does not undo work already done. Don't approve anything whose target or effect you can't identify. Ask for a plain-language explanation or a draft first. (Official: [Approvals](https://docs.x.ai/grok-bot/approvals-security-and-privacy))

**13.** Auto-review rules live in Settings → General → Auto-review. "Ask first" always wins over "Allow automatically." Write narrow rules and avoid broad ones like "allow everything in the browser." Each connector's page also lets you set every tool to Always allow, Auto-review, Needs approval, or Blocked. (Official: [Approvals](https://docs.x.ai/grok-bot/approvals-security-and-privacy); [Grok Bot changelog v1.2.3, Nov 18, 2026](https://x.ai/bot/changelog))

**14.** An approval from a chat you started waits until you answer. An approval from a routine, an incoming message, or other background work expires after 30 minutes; the card shows Expired and the action doesn't run, so ask the bot to try again. Sending a new message, or changing Auto-review settings, also closes open cards in that chat. (Official: [Approvals](https://docs.x.ai/grok-bot/approvals-security-and-privacy))

**15.** With 1Password, make a separate vault just for Grok Bot holding only the logins your bots need, and connect that vault, not your whole account. ([@heyrobinai](https://x.com/heyrobinai/status/2111806812148437333))

## Saving usage

**16.** Routine frequency is the #1 usage driver: an hourly schedule or a busy Slack trigger can use a week of usage in a day. Pause what you don't need and widen schedules before upgrading. (Official: [Routines help](https://cursor.com/help/grok-bot/routines))

**17.** 8-step order: slow your fastest routine, run routines in working hours only, move routines off your chat bot, duplicate long-running chats, point routines at a skill that stays silent when nothing's new, prefer connectors over the browser, script rule-based bulk work, keep on-demand off while testing. ([@GrokBotRadar](https://x.com/GrokBotRadar/status/2111513393538732162))

**18.** Routine-audit prompt: classify each routine as KEEP / SLOW DOWN / EVENT TRIGGER / CHANGE CHECK / RETIRE, rank by usage saved, and "don't make any changes until I approve." ([@Michael_Fenech_](https://x.com/Michael_Fenech_/status/2111478843202818102))

**19.** Turn mechanical "is there work?" checks into a tiny script that runs first and only wakes the bot when there is something to do. ([@wavegod](https://x.com/wavegod/status/2112961302767493490))

**20.** Find routines you're running by hand: "Look through the prompts I've sent to my different Bots. Which of these should turn into a routine or its own Bot?" Same check daily = routine; "when X happens" = trigger. ([@GrokBotRadar](https://x.com/GrokBotRadar/status/2114285625688137775))

**21.** Usage limits are per week. On-demand usage (if on) continues past it up to your monthly cap, and a running task can finish slightly past the cap. (Official: [Plans and billing](https://prod.cursor.com/help/grok-bot/plans), [FAQs](https://cursor.com/help/grok-bot/faqs))

**22.** **Bot-to-bot messages cost usage.** Every message one bot sends another runs a turn, and every turn counts toward your week. An idle bot can still be woken by your other bots, and telling bots to "stay quiet" is only a hint. For multi-step jobs, run the work in one bot that uses subagents, which finish and stop, and delete bots you no longer use (save the chat first, since deleting clears it). ([@GrokBotRadar](https://x.com/GrokBotRadar/status/2121914113173729454))

## Writing good routines and skills

**23.** Go Task → Fix → Skill → Test → Routine, not Prompt → Routine. Automate last. ([@Michael_Fenech_](https://x.com/Michael_Fenech_/status/2106352565528977469); Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**24.** Turn a role into a durable bot in six steps. Put the job, sources, output format and boundaries in the bot's description; run one real task with a safe scope; correct it until it's reviewable without you; save it as a skill and test it on a second input; add a routine only after retries and failure cases are defined; keep external actions behind approval. (Official: [Use cases](https://docs.x.ai/grok-bot/use-cases))

**25.** A good skill states when to use it, required inputs/access, the steps, how to validate, what to return, and what needs approval. (Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**26.** When **Teach a task** is available, demonstrate a browser workflow once instead of writing every step. Open a one-to-one chat and its computer view, choose Teach a task, describe the result, perform it, then review the draft skill and test it on a safe example before scheduling. Recording covers visible computer interaction for up to ten minutes and does not record microphone audio, so don't type secrets during the demo. If the control isn't there yet, ask the bot to save a skill from written instructions. (Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**27.** When creating a routine, confirm the owning bot, schedule and time zone, input source, expected result, approval boundary, and what to do if a source is missing. (Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**28.** Check the routine's time zone and "When to run". Schedules use Settings → Bot → Timezone (auto-detect follows the current computer). After asking for a schedule in plain words, open the routine and read When to run, which shows the saved schedule in words; choose Edit if it isn't what you meant. (Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**29.** Include a no-data / stale-data policy and say where to report partial completion; re-test after a website or source changes. (Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**30.** A new routine waits for its next scheduled time; use Test to try it now, and remember Test does real work, so use safe inputs. (Official: [Routines help](https://cursor.com/help/grok-bot/routines))

**31.** No Test button? Do a dry run in chat. Some routines don't show Test. Ask the bot to do the same work once in chat with a safe input, then watch the first scheduled run before relying on it. (Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**32.** Limits to know: up to 50 routines per bot, schedules at least 5 minutes apart, and deleting a routine can't be undone. (Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**33.** Routines have hourly caps. All your routines together can run up to 300 times an hour, and any one routine up to 200 times an hour. Past either limit a run fails with `Automation run rate limit exceeded`. If one routine keeps hitting it, narrow its trigger or widen its schedule. (Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**34.** Prefer narrow event triggers over broad listeners like "every new message," which create noise and burn usage. (Official: [Work with Grok Bot](https://cursor.com/docs/grok-bot/work))

**35.** Event triggers only see new activity. A routine triggered by Slack, GitHub, Linear, Sentry, PagerDuty, email or a webhook ignores events from before the trigger existed, so it will not backfill old issues or messages. Run a one-time catch-up task in chat if you need history. (Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**36.** Put the job, sources, output format and standing boundaries in the bot's description, then run one real task before automating. (Official: [Use cases](https://docs.x.ai/grok-bot/use-cases))

**37.** For research, give the bot a finish line: one measurable outcome, primary sources first, evidence beside claims, and an explicit stop condition. ([@ludoonchart](https://x.com/ludoonchart/status/2107191775433543884))

**38.** A routine that loses a connector sign-in pauses its scheduled runs until you sign back in. The reconnect prompt also arrives as a notification and as a Slack or Teams DM. (Official: [Grok Bot changelog](https://x.ai/bot/changelog))

**39.** A routine can read the earlier conversation in the chat it runs in. (Official: [Grok Bot changelog](https://x.ai/bot/changelog))

## Useful extras

**40.** Move your ChatGPT or Claude memory in: ask the old AI to export its memories of you, then tell Grok Bot "Import this memory." Skim and delete anything first. ([@GrokBotRadar](https://x.com/GrokBotRadar/status/2114651560177435049))

**41.** Give your bot its own inbox and forward it messy stuff (bills, forms, threads). You get one address per account and it can't be renamed, so pick carefully. ([@BotMeetUps](https://x.com/BotMeetUps/status/2113953564787880232))

**42.** Name the bot's email after a "chief of staff" persona rather than yourself, since copying in "you" reads oddly. ([@petergyang](https://x.com/petergyang/status/2108624122339287335))

**43.** iPhone: the Action Button can launch Grok Bot voice chat (iPhone 15 Pro or newer). ([@GrokBotPro](https://x.com/GrokBotPro/status/2114688509193683083))

**44.** Ask your bot where you're spending the most usage. ([@sawi1900](https://x.com/sawi1900/status/2107287460380131534))

**45.** **Bots can join meetings.** On Team, Enterprise and Ultra plans, a bot can join a Google Meet, Zoom or Microsoft Teams call from a link, answer in the meeting chat, and send a summary afterward. Microsoft Teams for Team bots needs a team admin to turn it on and a Teams admin to approve it. (Official: [Grok Bot changelog, Nov 11, 2026](https://x.ai/bot/changelog))

**46.** Teach your bot the official guides. Load the official Grok Bot guides and articles into a knowledge base so the bot knows how the product works. ([@unicodef1wn](https://x.com/unicodef1wn/status/2123802103374110786))

## Privacy-removal recheck schedules

**47.** Data brokers often re-list people, which is why most removal bots here recheck: [Remove Me](../categories/people-search-and-data-brokers.md#bot-qlDBDdHjGkHD9pka-9fRy) ([@OutworkVentures](https://x.com/OutworkVentures)) rechecks in 30 days; [Privacy Scrubber](../categories/people-search-and-data-brokers.md#bot-ZSQK72Iear_ykfnpTIOHQ), [Spam-Call Scrubber (Arash)](../categories/people-search-and-data-brokers.md#bot-fUj6TYhiW_cjtzWvbsFgz) ([@MinimalDuck](https://x.com/MinimalDuck)) and [Invisible Man](../categories/people-search-and-data-brokers.md#bot-avOGLCUGcrQ0T23v2lENG) recheck monthly (per their descriptions on this list). Run **one** recheck routine per site family, not one per bot.

[← Back to README](../README.md)
