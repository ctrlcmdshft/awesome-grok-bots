# Tips & Tricks

[← Back to README](../README.md)

Tips that came from a post or page link to it. Official means an xAI Grok Bot doc or guide. Tips 7 and 33 point to bots on this list.

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

## Safety and approval habits

**8.** Put boundaries in the request: say what the bot may do and where it must stop (sending, publishing, purchases, deleting, permissions, accepting terms). (Official: [Approvals, security, and privacy](https://docs.x.ai/grok-bot/approvals-security-and-privacy))

**9.** An approval controls the proposed action; it does not undo work already done. Don't approve anything whose target or effect you can't identify. Ask for a plain-language explanation or a draft first. (Official: [Approvals](https://docs.x.ai/grok-bot/approvals-security-and-privacy))

**10.** Auto-review rules live in Settings → General → Auto-review. "Ask first" always wins over "Allow automatically." Write narrow rules and avoid broad ones like "allow everything in the browser." (Official: [Approvals](https://docs.x.ai/grok-bot/approvals-security-and-privacy))

**11.** Approvals from routines or other bots expire after about 10 minutes if you don't answer; ask the bot to retry. (Official: [Approvals](https://docs.x.ai/grok-bot/approvals-security-and-privacy))

**12.** With 1Password, make a separate vault just for Grok Bot holding only the logins your bots need, and connect that vault, not your whole account. ([@heyrobinai](https://x.com/heyrobinai/status/2111806812148437333))

## Saving usage

**13.** Routine frequency is the #1 usage driver: an hourly schedule or a busy Slack trigger can use a week of usage in a day. Pause what you don't need and widen schedules before upgrading. (Official: [Routines help](https://cursor.com/help/grok-bot/routines))

**14.** 8-step order: slow your fastest routine, run routines in working hours only, move routines off your chat bot, duplicate long-running chats, point routines at a skill that stays silent when nothing's new, prefer connectors over the browser, script rule-based bulk work, keep on-demand off while testing. ([@GrokBotRadar](https://x.com/GrokBotRadar/status/2111513393538732162))

**15.** Routine-audit prompt: classify each routine as KEEP / SLOW DOWN / EVENT TRIGGER / CHANGE CHECK / RETIRE, rank by usage saved, and "don't make any changes until I approve." ([@Michael_Fenech_](https://x.com/Michael_Fenech_/status/2111478843202818102))

**16.** Turn mechanical "is there work?" checks into a tiny script that runs first and only wakes the bot when there is something to do. ([@wavegod](https://x.com/wavegod/status/2112961302767493490); bot on this list: [Script This Routine](../categories/bot-tools.md#bot-9E8iw2zlg2fTWzUT6RUsP) ([@Kevin\_Logan](https://x.com/Kevin_Logan)))

**17.** Find routines you're running by hand: "Look through the prompts I've sent to my different Bots. Which of these should turn into a routine or its own Bot?" Same check daily = routine; "when X happens" = trigger. ([@GrokBotRadar](https://x.com/GrokBotRadar/status/2114285625688137775))

**18.** Usage limits are per week. On-demand usage (if on) continues past it up to your monthly cap, and a running task can finish slightly past the cap. (Official: [Plans and billing](https://prod.cursor.com/help/grok-bot/plans), [FAQs](https://cursor.com/help/grok-bot/faqs))

## Writing good routines and skills

**19.** Go Task → Fix → Skill → Test → Routine, not Prompt → Routine. Automate last. ([@Michael_Fenech_](https://x.com/Michael_Fenech_/status/2106352565528977469); Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**20.** A good skill states when to use it, required inputs/access, the steps, how to validate, what to return, and what needs approval. (Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**21.** When creating a routine, confirm the owning bot, schedule and time zone, input source, expected result, approval boundary, and what to do if a source is missing. (Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**22.** Include a no-data / stale-data policy and say where to report partial completion; re-test after a website or source changes. (Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**23.** A new routine waits for its next scheduled time; use Test to try it now, and remember Test does real work, so use safe inputs. (Official: [Routines help](https://cursor.com/help/grok-bot/routines))

**24.** Limits to know: up to 50 routines per bot, schedules at least 5 minutes apart, and deleting a routine can't be undone. (Official: [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations))

**25.** Prefer narrow event triggers over broad listeners like "every new message," which create noise and burn usage. (Official: [Work with Grok Bot](https://cursor.com/docs/grok-bot/work))

**26.** Put the job, sources, output format and standing boundaries in the bot's description, then run one real task before automating. (Official: [Use cases](https://docs.x.ai/grok-bot/use-cases))

**27.** For research, give the bot a finish line: one measurable outcome, primary sources first, evidence beside claims, and an explicit stop condition. ([@ludoonchart](https://x.com/ludoonchart/status/2107191775433543884))

## Useful extras

**28.** Move your ChatGPT or Claude memory in: ask the old AI to export its memories of you, then tell Grok Bot "Import this memory." Skim and delete anything first. ([@GrokBotRadar](https://x.com/GrokBotRadar/status/2114651560177435049))

**29.** Give your bot its own inbox and forward it messy stuff (bills, forms, threads). You get one address per account and it can't be renamed, so pick carefully. ([@BotMeetUps](https://x.com/BotMeetUps/status/2113953564787880232))

**30.** Name the bot's email after a "chief of staff" persona rather than yourself, since copying in "you" reads oddly. ([@petergyang](https://x.com/petergyang/status/2108624122339287335))

**31.** iPhone: the Action Button can launch Grok Bot voice chat (iPhone 15 Pro or newer). ([@GrokBotPro](https://x.com/GrokBotPro/status/2114688509193683083))

**32.** Ask your bot where you're spending the most usage. ([@sawi1900](https://x.com/sawi1900/status/2107287460380131534))

## Privacy-removal recheck schedules

**33.** Data brokers often re-list people, which is why most removal bots here recheck: [Remove Me](../categories/people-search-and-data-brokers.md#bot-qlDBDdHjGkHD9pka-9fRy) ([@OutworkVentures](https://x.com/OutworkVentures)) rechecks in 30 days; [Privacy Scrubber](../categories/people-search-and-data-brokers.md#bot-ZSQK72Iear_ykfnpTIOHQ), [Spam-Call Scrubber (Arash)](../categories/people-search-and-data-brokers.md#bot-fUj6TYhiW_cjtzWvbsFgz) and [Invisible Man](../categories/people-search-and-data-brokers.md#bot-avOGLCUGcrQ0T23v2lENG) recheck monthly (per their descriptions on this list). Run **one** recheck routine per site family, not one per bot.

[← Back to README](../README.md)
