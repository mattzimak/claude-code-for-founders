# Claude Code field guide

135 entries · last verified 2026-09-09 · 135 links checked · 0 dead

One founder's field guide to running a company on Claude Code: the skills I install, the setups I copied, the rules I keep, and the people worth learning from. It is not a directory of everything that exists - if something is here, it earned its place in real work. Suggest a link by opening an issue (see [CONTRIBUTING.md](CONTRIBUTING.md)).

Descriptions are my own notes where I wrote one. Where I only saved a link, the description is the repository's or the post's own summary. Ratings like `(Matt: 8/10)` are my personal scores.

## Contents

- [Start here](#start-here)
- [Learn](#learn)
- [Agent teams and subagents](#agent-teams-and-subagents)
- [Prompting](#prompting)
- [Skills](#skills)
  - [General](#general)
  - [Token burn & models](#token-burn--models)
  - [Webdesign taste skills](#webdesign-taste-skills)
  - [Webdesign dev skills](#webdesign-dev-skills)
  - [Webdesign MCP & UI elements](#webdesign-mcp--ui-elements)
  - [Project management](#project-management)
  - [Development](#development)
  - [Research](#research)
  - [Image & Video Editing](#image--video-editing)
  - [Marketing - Content & Writing](#marketing---content--writing)
  - [Marketing - Ads & SEO](#marketing---ads--seo)
- [Collections](#collections)
- [Field notes](#field-notes)
  - [General best practices](#general-best-practices)
  - [Plan vs bypass mode](#plan-vs-bypass-mode)
  - [Effort](#effort)
  - [Prompting basics](#prompting-basics)
  - [Structure](#structure)
  - [CLAUDE.md](#claudemd)
  - [Security and passwords](#security-and-passwords)
  - [Context](#context)
  - [Hooks](#hooks)
  - [Personal assistant](#personal-assistant)
- [Tools and memory](#tools-and-memory)
- [n8n with Claude Code](#n8n-with-claude-code)
- [Other useful lists](#other-useful-lists)
- [How this list is built](#how-this-list-is-built)
- [License](#license)

## Start here

What I would send a founder who has one evening: my highest-rated picks and the first entries I wrote a reason for. The full list follows.

- [apple-design](https://github.com/emilkowalski/skills/tree/main/skills/apple-design) - Apple's fluid-interfaces philosophy (WWDC 2018 "Designing Fluid Interfaces") translated to the web: springs, velocity inheritance, momentum projection, interruptible gestures, reduced-motion. Dense and genuinely educational. (Matt: 9/10) · 36k stars · MIT · updated 2026-08 · Skills / Webdesign taste skills
- [design-taste-frontend](https://github.com/Leonxlnx/taste-skill/tree/main/skills/taste-skill) - The flagship (266.5K installs, 1,200 lines). Reads the brief before generating: infers page kind, audience, vibe and constraints, outputs a one-line "Design Read", then pulls only the contextual rules that fit instead of one house style for everything. (Matt: 9/10) · 85k stars · MIT · updated 2026-08 · Skills / Webdesign taste skills
- [emil-design-eng](https://github.com/emilkowalski/skills/tree/main/skills/emil-design-eng) - Emil Kowalski's full design-engineering philosophy (679 lines): UI polish, when to animate, the invisible details that make software feel right. Mild course-plug in the intro, content is excellent. (Matt: 8/10) · 36k stars · MIT · updated 2026-08 · Skills / Webdesign taste skills
- [find-animation-opportunities](https://github.com/emilkowalski/skills/tree/main/skills/find-animation-opportunities) - Restraint-first finder built on "You Don't Need Animations": sweeps a UI for moments that genuinely deserve motion, rejects most candidates, proposes exact values. Read-only. (Matt: 8/10) · 36k stars · MIT · updated 2026-08 · Skills / Webdesign taste skills
- [imagegen-frontend-web](https://github.com/Leonxlnx/taste-skill/tree/main/skills/imagegen-frontend-web) - Directs image generation of website design references: one horizontal image per section (never a compressed full-page board), enforced composition variety, one palette across all images. Pairs with banana / higgsfield-generate. (Matt: 8/10) · 85k stars · MIT · updated 2026-08 · Skills / Webdesign taste skills
- [improve-animations](https://github.com/emilkowalski/skills/tree/main/skills/improve-animations) - Senior-advisor motion audit: surveys a codebase's animation code, produces prioritized findings plus self-contained implementation plans a cheaper model can execute. Read-only. (Matt: 8/10) · 36k stars · MIT · updated 2026-08 · Skills / Webdesign taste skills
- [redesign-existing-projects](https://github.com/Leonxlnx/taste-skill/tree/main/skills/redesign-skill) - Scan, diagnose, fix sequence for upgrading existing sites: audits typography, spacing and generic AI patterns with concrete checks, improves within the existing stack rather than rewriting. (Matt: 8/10) · 85k stars · MIT · updated 2026-08 · Skills / Webdesign taste skills
- [review-animations](https://github.com/emilkowalski/skills/tree/main/skills/review-animations) - Reviews animation code against a strict craft bar with a separate STANDARDS.md; "default to flagging, approval is earned". NOTE: ships with disable-model-invocation, so it never auto-fires - invoke explicitly. (Matt: 8/10) · 36k stars · MIT · updated 2026-08 · Skills / Webdesign taste skills
- [antfarm](https://github.com/snarktank/antfarm) - Free, open-source multi-agent orchestration on OpenClaw - YAML-defined pipelines with a fresh context per AI agent, and pre-built workflows for feature development, security audits, and bug fixes. Why: The cleanest way we have seen to run a team of OpenClaw agents without extra infrastructure. · 2.5k stars · MIT · updated 2026-02 · Skills / Development
- [find-skills](https://github.com/vercel-labs/skills) - Discovers and installs skills from the open ecosystem - checks the skills.sh leaderboard, ranks by installs and source reputation, and installs straight from GitHub. Why: The package manager habit: instead of building from scratch, we check what already exists and vet it. · 30k stars · MIT · updated 2026-09 · Skills / General
- [Frontend design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) - Anthropic's official frontend design skill; encodes Vercel-style web interface guidelines, component patterns, and accessibility rules so Claude produces production-grade UI out of the box. Why: Raises the floor: UI output goes from generic to shippable without extra prompting. · 175k stars · updated 2026-09 · Skills / Webdesign dev skills
- [higgsfield-generate](https://github.com/higgsfield-ai/skills) - Gives Claude one-command generation across 30+ models - Nano Banana 2/Pro for images, Seedance 2.0 for video with native audio, plus Kling, Veo, GPT Image 2, 3D, and Marketing Studio - including image-to-video, reframe, and virality scoring. (official Higgsfield · uses your connected Higgsfield MCP/account) Why: Powers our creative AI guides, including the champagne video - one skill instead of five tabs. · 910 stars · MIT · updated 2026-08 · Skills / Image & Video Editing

## Learn

Videos and threads that taught me how Claude Code actually works - start here if you are new to it.

- [AI marketing Masterclass: From beginner to expert in 60 minutes](https://www.youtube.com/watch?v=fVUlrpaWNxg) - I sit down with James Dickerson, a growth marketer, Claude Code power user, and the mind behind The Boring Marketer, to watch him build an entire marketing system live from the terminal.
- [Automate Your Life with Claude Code in 40 Minutes | Moritz Kremb](https://www.youtube.com/watch?v=ACRd0Ikg_KI) - The honest tradeoffs: OpenClaw vs. Claude Code.
- [Build & Sell with Claude Code (10+ Hour Course)](https://www.youtube.com/watch?v=mpALXah_PBg) - This is the complete Claude Code course. Trust me, save this for later.
- [Build an agent that improves itself in 20 minutes (CyrilXBT on X, video)](https://x.com/cyrilXBT/status/2076353923695227108) - CyrilXBT's clip of an Anthropic engineer's AI Engineer World's Fair talk, framed as 'Fable 5 is already smarter than we know how to use, the bottleneck was never the AI, it is you'. The talk shows how to build a self-improving agent with no extra tools and no extra cost; the post quotes his own X article on 60 Fable 5 workflows.
- [Claude Code Just Got an Agent Dashboard](https://www.youtube.com/watch?v=ZAaxx3qyT8g) - Claude Code just dropped Agent View, a new way to run and manage multiple sessions from a single terminal tab.
- [Claude Code Skills Just Got Even Better](https://www.youtube.com/watch?v=RAZVk5NPNtE) - Claude Code just dropped a major update to how skills work.
- [Designing loops with Claude Fable 5 (Divyanshi Sharma on Instagram)](https://www.instagram.com/p/DaqH6G0kn5P) - 11-slide carousel on building self-improving systems that run on repeat: a self-correction loop where a separate grader model scores the output against a rubric until it passes (Claude Code /goal versus Outcomes in Claude Managed Agents), memory across sessions so the agent turns mistakes into rules it actually rereads, and the Parameter Golf benchmark where Fable 5 improved a training pipeline...
- [Eyad Khrais - Claude Code Tutorial Thread](https://x.com/eyad_khrais/status/2010076957938188661) - Viral 4.8M-view thread by ex-Amazon/Disney/Capital One CTO breaking down Claude Code's three power features: Skills, Hooks, and Commands - with concrete examples for each.
- [How to Make Claude Code Your AI Engineering Team](https://www.youtube.com/watch?v=wkv2ifxPpF8) - GStack is an open-source toolkit built by YC President & CEO Garry Tan that turns Claude Code into an AI engineering team - with skills for office hours, design, code review, QA, and browser testing.
- [Loop engineering, clearly explained (Charlie Hills on Instagram)](https://www.instagram.com/p/DZzbZzVCCV-?img_index=1) - 9-slide carousel with the six-part loop Charlie runs in Claude Code without writing code: /init writes your standards into CLAUDE.md, /goal sets the outcome and the rubric score it cannot stop below, /agents spins up a strategist, a writer and a designer with one job each, a separate QA agent grades every draft (LLM-as-judge), MEMORY.md saves every correction as a rule, and a scheduled Routine...
- [Stop prompting Claude, use loops instead (Divjot Sahni on Instagram)](https://www.instagram.com/p/DaA-8wLE2NX) - 8-slide carousel on the five loops Claude Code runs on its own once you give it a goal and a finish line, namely plan-act-check, self-correction, tool use, subagent fan-out and stop conditions, plus the built-in /loop command that reruns a task or a whole slash command on an interval or paces itself. The plain-English case for handing over the whole job instead of feeding it the next instruction.
- [The Four Agent Loops in Claude Code · TheVibeFounder](https://thevibefounder.com/r/loops) - Turn-based, goal-based, time-based, proactive. The four Claude Code agent loops, and how much you hand off at each rung.

## Agent teams and subagents

How I split work between subagents, and the two setups worth copying.

- [agency-agents](https://github.com/msitarzewski/agency-agents) - A complete AI agency in Claude Code: frontend wizards, Reddit community ninjas, whimsy injectors, and reality checkers - each agent is a specialized expert with personality, processes, and proven deliverables. · 151k stars · MIT · updated 2026-09 · also: [agencyagents.app](https://agencyagents.app)
- [gstack](https://github.com/garrytan/gstack) - Garry Tan's exact Claude Code setup: 15 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA. · 132k stars · MIT · updated 2026-09
- [Skills vs MCP (The New Stack)](https://thenewstack.io/skills-vs-mcp-agent-architecture) - "Skills (Markdown) are the knowledge layer; MCP is the execution layer," with a 100x token-cost difference for equivalent functionality. The article also covers Brad Feld's open-sourced CompanyOS, which runs an operation on 12 Markdown files plus 8 MCPs, each skill with a standalone mode that works without MCP.
- Sub-agents for atomic tasks ONLY - Don't create CEO agents and product agents. Keep shared context in ONE session. Sub-agents lose the reasoning chain. Bring work to the context, not context to the work.

## Prompting

My own prompt patterns for Fable 5 - copy them as they are.

- [10 Claude prompts to build a mobile app (Hamidullah Khan on Threads)](https://www.threads.com/@iamkhanphd/post/DV8kMGKDrm8?slof=1) - Hamidullah Khan's Threads post with 10 Claude prompts for building a mobile app end to end, starting with an architecture prompt that makes Claude act as a senior SwiftUI engineer and propose MVVM, folder structure and data flow before it writes code, then one prompt per stage of the build. Each prompt sits in a reply under the post.
- [5 Claude prompts to grow an Instagram account (Camila Markson on Instagram)](https://www.instagram.com/p/DWHfrCHGc6r) - Camila Markson's 7-slide carousel with the five Claude prompts behind her claim of 3,000 new followers in a day: analyse five top-performing reels in your niche and explain why they went viral, write ten scroll-stopping hooks, build a 7-day content strategy, rewrite a caption with emotional storytelling and a strong call to action, and generate five carousel ideas built for saves and shares.
- [500 Claude prompts that replace a $10K marketing agency (CyrilXBT on X)](https://x.com/cyrilxbt/status/2042980564194521176) - CyrilXBT's X article with 500 Claude prompts organised by the agency role they replace, content strategist, copywriter, social media manager, SEO and blog writer, brand consultant, customer research, email marketing and video scripts, each a fill-in-the-blanks brief that treats Claude like a senior employee.
- [7 Claude prompts to run your business (Camila Markson on Instagram)](https://www.instagram.com/p/DWfCQdLEjDL) - 9-slide carousel with the seven prompts Camila Markson says she uses every day so Claude works like a $5K a month assistant: a 7-day content machine in your brand voice, a blunt offer audit of your sales page, a 5-email welcome sequence, a 30-second Reels script, a 3-message DM follow-up, a 10-slide carousel builder and a weekly CEO debrief on your numbers. Copy-paste prompts, no tools required.
- [Content OS built with Claude Code prompts (Tyler Germain on Instagram)](https://www.instagram.com/p/DV9_kEmEVxM?img_index=2) - Tyler Germain's 8-slide carousel with the prompts he used to build a full content OS in a week: a Next.js, Tailwind and shadcn/ui dashboard with an Instagram manager, a Metricool-fed analytics page, a content calendar, a competitor tracker and an RSS news consolidator, one plain-English prompt per page, plus a CLAUDE.md that documents the stack and the decisions.
- Fable 5 can report a step as done before verifying it, to fix, insert always this prompt:
  ```text
  Before reporting progress, audit each claim against a tool result from this session.

  Only report work you can point to evidence for. If something is not verified, say so.

  If a step failed, state that with the output. Do not report success you cannot prove.
  ```
- Blindspot pass - Ask Claude to surface your unknown unknowns before starting unfamiliar work.
- > "Can you do a blindspot pass to help me figure out my relevant unknown unknowns and help me prompt you better."
- Brainstorms & prototypes - Ask for several wildly different options to react to instead of one answer.
- > "Make me an HTML page with 4 wildly different design directions so I can react to them."
- Interviews - Have Claude interview you one question at a time to resolve ambiguity.
- > "Prioritize questions where my answer would change the architecture."
- References - Point Claude at existing code and have it reimplement the same semantics.
- > "This Rust crate in vendor/rate-limiter implements the exact backoff behavior I want. Read it and reimplement the same semantics in our TypeScript API client."
- Implementation notes - Have Claude keep a running log and handle edge cases without stopping.
- > "Keep an implementation-notes.md file. If you hit an edge case, pick the conservative option, log it under 'Deviations', and keep going."
- Quizzes - After a change, ask for a report plus a quiz to verify your own understanding.
- > "Give me a HTML report on the changes with context, intuition, what was done - and a quiz at the bottom that I must pass."

## Skills

The skills I install, grouped by what they are for. Star counts and licenses come from GitHub and are refreshed weekly.

### General

- [Access to Codex](https://github.com/openai/codex-plugin-cc) - Use OpenAI Codex from within Claude Code to review code, run tasks in parallel, or delegate subtasks to a separate coding agent. · 32k stars · Apache-2.0 · updated 2026-07
- [AI Project Starter for Claude Code](https://github.com/jlaran/AI-Project-Starter-Claude) - Opinionated project scaffold with pre-configured CLAUDE.md, folder structure, and best-practice defaults to get any Claude Code project started cleanly. · 8 stars · MIT · updated 2026-01
- [Claude Mem](https://github.com/thedotmack/claude-mem) - Persistent context across sessions for any agent; captures everything Claude does, compresses it with AI, and injects relevant context back into future sessions via hybrid semantic and keyword search. · 93k stars · Apache-2.0 · updated 2026-09
- [Claude Video](https://github.com/bradautomates/claude-video) - See frames in videos - Give Claude the ability to watch any video. /watch downloads, extracts frames, transcribes, hands it all to Claude. · 16k stars · MIT · updated 2026-07
- [find-skills](https://github.com/vercel-labs/skills) - Discovers and installs skills from the open ecosystem - checks the skills.sh leaderboard, ranks by installs and source reputation, and installs straight from GitHub. Why: The package manager habit: instead of building from scratch, we check what already exists and vet it. · 30k stars · MIT · updated 2026-09
- [GSD (Get Sh\*t Done)](https://www.reddit.com/r/ClaudeAI/comments/1q4yjo0/get_shit_done_the_1_cc_framework_for_people_tired) - Context engineering framework for reliable Claude Code with planning and subagent orchestration. · also: [youtube.com](https://www.youtube.com/watch?v=8_7Sq6Vu0S4)
- [Obsidian Skills](https://github.com/kepano/obsidian-skills) - Agent skills that teach Claude Code how to natively create and edit Obsidian-specific formats including Markdown with wikilinks, Canvas files, and Bases, and interact with the Obsidian CLI. · 48k stars · MIT · updated 2026-06
- [openai/whisper](https://github.com/openai/whisper) - General-purpose speech recognition model trained on 680,000 hours of multilingual audio; performs transcription, translation, and language identification with state-of-the-art accuracy. · 108k stars · MIT · updated 2026-08
- [openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) - Unlimited persistent memory for an OpenClaw agent - everything it learns survives restarts and long gaps, retrievable by meaning rather than keywords. Why: An assistant that forgets last month is a chatbot. Memory is what makes it feel like staff. · 799 stars · updated 2026-09
- [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) - Converts any documentation website, GitHub repo, or PDF into a ready-to-use Claude skill with automatic conflict detection. · 14k stars · MIT · updated 2026-09
- [skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) - Build and optimize skills based on Anthropic's own best practices; lets an agent do deep research on a topic (like SEO) and iteratively refine the skill until it's perfect. Why: The skill that makes all the other skills - we used it to build our client-specific ones. · 175k stars · updated 2026-09

### Token burn & models

- [Caveman](https://github.com/JuliusBrussee/caveman) - Cuts 65% of token usage by instructing Claude to respond in compressed, caveman-style shorthand - ideal for long sessions where context budget matters. · 104k stars · updated 2026-09 · also: [linkedin.com](https://www.linkedin.com/posts/walid-boulanouar_i-saved-75-on-my-claude-code-bill-by-changing-share-7455179110076837888-6fvv)
- [Omniroute](https://github.com/diegosouzapw/OmniRoute) - Never stop coding. Free MIT AI gateway: one endpoint, 352 providers (150+ free), 1200+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. · 63k stars · MIT · updated 2026-09 · also: [omniroute.online](https://omniroute.online)
- [Ponytail](https://github.com/DietrichGebert/ponytail#install) - Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. · 132k stars · MIT · updated 2026-09
- [qmd-skill](https://github.com/levineam/qmd-skill) - Cuts an OpenClaw agent's token usage by up to 95% by compressing context handling - the difference between a cheap always-on assistant and an expensive one. Why: Always-on agents burn tokens around the clock; this is the single biggest cost lever we know. · 696 stars · updated 2026-02
- [STE Writing Skill](https://github.com/woosal1337/blog/tree/main/videos/ep01-the-cure-for-ai-slop/asd-ste100) - A global Claude skill that rewrites technical prose (READMEs, PR descriptions, error messages, runbooks, release notes, code comments - never code or marketing copy) into ASD-STE100 Simplified Technical English, stripping AI-slop form. Two modes (strict for procedures/safety, STE-flavored for general docs) plus a 7-point self-lint; adapted to ban em/en dashes per Matt's hyphen-only rule. · 511 stars · updated 2026-09

### Webdesign taste skills

- [animation-vocabulary](https://github.com/emilkowalski/skills/tree/main/skills/animation-vocabulary) - Reverse-lookup glossary: describe a motion effect vaguely ("the bouncy thing when a popover opens") and get the precise term to prompt with. Useful, narrow. (Matt: 6/10) · 36k stars · MIT · updated 2026-08
- [apple-design](https://github.com/emilkowalski/skills/tree/main/skills/apple-design) - Apple's fluid-interfaces philosophy (WWDC 2018 "Designing Fluid Interfaces") translated to the web: springs, velocity inheritance, momentum projection, interruptible gestures, reduced-motion. Dense and genuinely educational. (Matt: 9/10) · 36k stars · MIT · updated 2026-08
- [brandkit](https://github.com/Leonxlnx/taste-skill/tree/main/skills/brandkit) - Image-generation direction for brand-guidelines boards, logo systems and identity decks that look studio-made. For pitch and identity work. (Matt: 7/10) · 85k stars · MIT · updated 2026-08
- [design-taste-frontend](https://github.com/Leonxlnx/taste-skill/tree/main/skills/taste-skill) - The flagship (266.5K installs, 1,200 lines). Reads the brief before generating: infers page kind, audience, vibe and constraints, outputs a one-line "Design Read", then pulls only the contextual rules that fit instead of one house style for everything. (Matt: 9/10) · 85k stars · MIT · updated 2026-08
- [emil-design-eng](https://github.com/emilkowalski/skills/tree/main/skills/emil-design-eng) - Emil Kowalski's full design-engineering philosophy (679 lines): UI polish, when to animate, the invisible details that make software feel right. Mild course-plug in the intro, content is excellent. (Matt: 8/10) · 36k stars · MIT · updated 2026-08
- [find-animation-opportunities](https://github.com/emilkowalski/skills/tree/main/skills/find-animation-opportunities) - Restraint-first finder built on "You Don't Need Animations": sweeps a UI for moments that genuinely deserve motion, rejects most candidates, proposes exact values. Read-only. (Matt: 8/10) · 36k stars · MIT · updated 2026-08
- [gpt-taste](https://github.com/Leonxlnx/taste-skill/tree/main/skills/gpt-tasteskill) - Awwwards/GSAP-heavy landing pages: forced layout randomization via a simulated dice-roll, AIDA structure, strict motion patterns. Breaks layout repetition but rigid and gimmicky. (Matt: 6/10) · 85k stars · MIT · updated 2026-08
- [high-end-visual-design](https://github.com/Leonxlnx/taste-skill/tree/main/skills/soft-skill) - "Premium agency" aesthetic: hard banned-list (Inter, harsh shadows, Bootstrap grids) plus a variance engine picking from texture archetypes (ethereal glass, editorial luxury, soft structuralism). Slightly LARP-y persona, concrete rules. (Matt: 7/10) · 85k stars · MIT · updated 2026-08
- [image-to-code](https://github.com/Leonxlnx/taste-skill/tree/main/skills/image-to-code-skill) - Design-image-first workflow: generate large section-specific reference images, analyze deeply, implement to match. Codex-flavored phrasing but the discipline transfers. (Matt: 7/10) · 85k stars · MIT · updated 2026-08
- [imagegen-frontend-mobile](https://github.com/Leonxlnx/taste-skill/tree/main/skills/imagegen-frontend-mobile) - Mobile counterpart: app-native screen concepts in subtle phone mockups with multi-screen consistency. Images only, no code. (Matt: 7/10) · 85k stars · MIT · updated 2026-08
- [imagegen-frontend-web](https://github.com/Leonxlnx/taste-skill/tree/main/skills/imagegen-frontend-web) - Directs image generation of website design references: one horizontal image per section (never a compressed full-page board), enforced composition variety, one palette across all images. Pairs with banana / higgsfield-generate. (Matt: 8/10) · 85k stars · MIT · updated 2026-08
- [improve-animations](https://github.com/emilkowalski/skills/tree/main/skills/improve-animations) - Senior-advisor motion audit: surveys a codebase's animation code, produces prioritized findings plus self-contained implementation plans a cheaper model can execute. Read-only. (Matt: 8/10) · 36k stars · MIT · updated 2026-08
- [industrial-brutalist-ui](https://github.com/Leonxlnx/taste-skill/tree/main/skills/brutalist-skill) - Two committed archetypes (Swiss industrial print or CRT/tactical terminal, never mixed) with specific type systems and simulated analog degradation. Great when the brief calls for it. (Matt: 7/10) · 85k stars · MIT · updated 2026-08
- [minimalist-ui](https://github.com/Leonxlnx/taste-skill/tree/main/skills/minimalist-skill) - Notion-like warm-monochrome editorial style: flat components, serif/sans/mono type architecture with named font stacks, bans on gradients, pills and AI copy cliches. Narrow by design, coherent in its niche. (Matt: 7/10) · 85k stars · MIT · updated 2026-08
- [redesign-existing-projects](https://github.com/Leonxlnx/taste-skill/tree/main/skills/redesign-skill) - Scan, diagnose, fix sequence for upgrading existing sites: audits typography, spacing and generic AI patterns with concrete checks, improves within the existing stack rather than rewriting. (Matt: 8/10) · 85k stars · MIT · updated 2026-08
- [review-animations](https://github.com/emilkowalski/skills/tree/main/skills/review-animations) - Reviews animation code against a strict craft bar with a separate STANDARDS.md; "default to flagging, approval is earned". NOTE: ships with disable-model-invocation, so it never auto-fires - invoke explicitly. (Matt: 8/10) · 36k stars · MIT · updated 2026-08
- [stitch-design-taste](https://github.com/Leonxlnx/taste-skill/tree/main/skills/stitch-skill) - Generates anti-generic DESIGN.md files in Google Stitch's semantic language; wired into the UI sourcing rule alongside the Stitch MCP. (Matt: 7/10) · 85k stars · MIT · updated 2026-08

### Webdesign dev skills

- [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) - Clone any website with a single command using AI coding agents; outputs a fully editable local copy of the target site's structure and styles. · 34k stars · MIT · updated 2026-08
- [anthropics/knowledge-work-plugins - design-critique](https://github.com/anthropics/knowledge-work-plugins) - Anthropic's open-source plugin repository for knowledge workers (16.8K stars), featuring the design-critique skill that delivers structured UX/UI critique by evaluating decisions across usability, hierarchy, clarity, and interaction quality. It is particularly useful for spotting weak UX patterns and suggesting concrete, actionable improvements. · 23k stars · Apache-2.0 · updated 2026-09
- [Brand Guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) - Encode your brand into a skill; auto-applies your colors, fonts, spacing, and tone of voice consistently across everything Claude outputs. · 175k stars · updated 2026-09
- [Canvas Design](https://github.com/anthropics/skills/blob/main/skills/canvas-design/SKILL.md) - Anthropic's official skill for creating visual art, posters, and compositions as real PNG/PDF files directly from Claude Code. · 175k stars · updated 2026-09
- [Figma Skills](https://github.com/figma/mcp-server-guide/tree/main/skills) - Official Figma skills that teach Claude Code how to read Figma files, extract design tokens, and implement designs with pixel-perfect accuracy via the Figma MCP server. (Figma MCP Writeup) · 2k stars · updated 2026-09 · also: [help.figma.com](https://help.figma.com/hc/en-us/articles/39166810751895-Figma-skills-for-MCP)
- [Frontend design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) - Anthropic's official frontend design skill; encodes Vercel-style web interface guidelines, component patterns, and accessibility rules so Claude produces production-grade UI out of the box. Why: Raises the floor: UI output goes from generic to shippable without extra prompting. · 175k stars · updated 2026-09
- [Huashu Design](https://github.com/alchaincyf/huashu-design) - A free alternative to Claude Design that runs inside Claude Code, turning a single sentence into finished prototypes, HTML slide decks, MP4 animations, or infographics in 3-30 minutes. Draws on 20 built-in design philosophies and uses Playwright to verify output in a real browser before delivery. · 24k stars · MIT · updated 2026-08
- [Impeccable](https://github.com/pbakaus/impeccable) - A design auditor that enforces 27 deterministic anti-pattern rules (no cheesy gradients, no Inter-for-everything, no cards-inside-cards) to catch AI slop before it ships. Includes 23 slash commands for auditing, polishing, and iterating on frontend designs directly inside Claude Code. Why: Catches AI-slop design before it ships; we run it on every UI change. · 66k stars · Apache-2.0 · updated 2026-09
- [inference-sh/skills - landing-page-design](https://github.com/inference-sh/skills) - inference.sh's agent skills library (483 stars), providing the landing-page-design skill that helps create higher-converting landing pages by improving structure, messaging hierarchy, CTAs, and visual layout. It balances aesthetics with conversion-oriented design principles to produce pages that both look good and perform well. · 730 stars · updated 2026-08
- [Playwright](https://github.com/microsoft/playwright) - Microsoft's browser automation framework that, when paired with Claude Code, opens your app in a real browser, takes a screenshot, and flags design issues before you ship. Supports Chromium, Firefox, and WebKit across 100+ browser styles and 20+ usability rules. · 95k stars · Apache-2.0 · updated 2026-09
- [Schoepplake/framer-motion-skill](https://github.com/Schoepplake/framer-motion-skill) - Production-grade animation patterns for React and Next.js using Motion (formerly Framer Motion). Covers correct imports, scroll animations, exit animations with AnimatePresence, stagger variants, layout animations, gesture animations, accessibility via useReducedMotion, and ready-to-use recipes (progress bar, counter, page transition, gradient shimmer). · 5 stars · updated 2026-06
- [taste-skill](https://github.com/Leonxlnx/taste-skill) - An anti-slop frontend framework with adjustable dials for layout variance, motion intensity, and visual density - soft, minimalist, brutalist, and redesign variants. · 85k stars · MIT · updated 2026-08
- [Theme Factory](https://github.com/anthropics/skills/blob/main/skills/theme-factory/SKILL.md) - Generate cohesive color palettes and typography systems you can apply across an entire product; maintained by Anthropic. · 175k stars · updated 2026-09
- [Top 5 Claude Code Front-End Skills](https://theaileverage.beehiiv.com/p/top-5-claude-code-front-end-skills) - Detailed tutorial on impeccable, Huashu design, UI/UX Max Pro, Taste skill, Playwright.
- [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) - A searchable design intelligence database - 161 reasoning rules, 67 UI styles, 161 color palettes, 57 font pairings - that generates a complete design system before a line of code is written. · 126k stars · MIT · updated 2026-09
- [vercel-labs/agent-skills - web-design-guidelines](https://github.com/vercel-labs/agent-skills) - Vercel's official collection of agent skills, containing the web-design-guidelines skill that reviews UI code against Vercel's web interface standards to catch design, UX and accessibility issues, with file-level feedback. Why: A second, stricter pair of eyes on layout and accessibility - complements impeccable well. · 30k stars · updated 2026-08

### Webdesign MCP & UI elements

- [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) - The official 21st.dev Magic MCP server itself. Described as "like v0 but in your Cursor/Windsurf/Cline" - an AI-driven tool that generates polished, production-ready UI components from natural language descriptions, with SVGL logo integration. · 5.8k stars · ISC · updated 2026-09
- [Google Stitch MCP](https://github.com/google-labs-code/stitch-skills) - Generate full UI screens from a text prompt, piped directly into Claude Code via MCP. · 8.3k stars · Apache-2.0 · updated 2026-08 · also: [stitch.withgoogle.com](https://stitch.withgoogle.com) · also: [stitch.withgoogle.com](https://stitch.withgoogle.com/docs/mcp/setup)
- [Shadcn-ui](https://github.com/shadcn-ui/ui) - A set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks. Open Source. Open Code. · 123k stars · MIT · updated 2026-09

### Project management

- [Linear](https://github.com/wrsmith108/linear-claude-skill) - Manage Linear issues, projects, and teams from Claude Code using MCP tools, SDK automation, and GraphQL API patterns. (Codex version by OpenAI) · 123 stars · MIT · updated 2026-07 · also: [github.com](https://github.com/openai/skills/tree/main/skills/.curated/linear)

### Development

- [antfarm](https://github.com/snarktank/antfarm) - Free, open-source multi-agent orchestration on OpenClaw - YAML-defined pipelines with a fresh context per AI agent, and pre-built workflows for feature development, security audits, and bug fixes. Why: The cleanest way we have seen to run a team of OpenClaw agents without extra infrastructure. · 2.5k stars · MIT · updated 2026-02
- [Code Reviewer](https://jeffallan.github.io/claude-skills/skills/quality/code-reviewer) - Use before opening a PR; delivers a full structured review covering what is broken, what is risky, what is messy, and what is solid.
- [Debug this](https://github.com/AlmogBaku/debug-skill) - Use when stuck on a bug; gives real breakpoints, lets you step through execution line by line, and inspect live variable state. · 317 stars · MIT · updated 2026-04
- [Feature Forge](https://jeffallan.github.io/claude-skills/skills/workflow/feature-forge) - Use before writing a single line of code; asks the right questions, thinks like both a PM and a dev, and hands you a full spec with requirements and acceptance criteria.
- [Git Worktrees](https://github.com/obra/superpowers/tree/main/skills/using-git-worktrees) - Creates isolated workspaces for multiple branches so you never lose your current context when switching between them. · 283k stars · MIT · updated 2026-09
- [LightRAG](https://github.com/hkuds/lightrag) - A fast, lightweight RAG system that enhances LLMs with graph-based retrieval, supporting multiple storage backends and multimodal data processing. · 39k stars · MIT · updated 2026-09
- [Mobile Apps](https://github.com/sleekdotdesign/agent-skills) - Agent skills for building and testing mobile apps from Claude Code, covering React Native and Expo workflows. · 572 stars · MIT · updated 2026-09
- [Playwright Skill](https://github.com/testdino-hq/playwright-skill) - Use before writing any implementation code; walks through the full TDD cycle: write the failing test, watch it fail, then write just enough to pass it. · 361 stars · MIT · updated 2026-09
- [RAG Architect](https://jeffallan.github.io/claude-skills/skills/data-ml/rag-architect) - Designs the full RAG pipeline for any vector search or knowledge base project: chunking, embeddings, retrieval, and reranking.
- [Secure Code Guardian](https://jeffallan.github.io/claude-skills/skills/security/secure-code-guardian) - If you’re building anything with auth, passwords, or user input, this writes secure code from the jump. no vulnerabilities you’ll regret later.
- [Spec Miner](https://jeffallan.github.io/claude-skills/skills/workflow/spec-miner) - Point at inherited code with zero documentation; reads everything, traces data flows, and writes the spec that should have been there from day one.
- [Supabase Agent Skills](https://github.com/supabase/agent-skills) - Official Supabase skills that teach AI agents how to interact with Supabase databases, auth, storage, and edge functions from Claude Code. · 2.6k stars · MIT · updated 2026-08
- [Superpowers](https://github.com/obra/superpowers) - Keeps context windows clean by dispatching isolated agents per task instead of one long session that drifts; covers the full software development workflow including brainstorming, planning, subagent-driven dev, TDD enforcement, code review, and git worktrees. Why: It is the backbone of how we build - every feature on this very website goes through its brainstorm and review steps. · 283k stars · MIT · updated 2026-09
- [The Fool](https://jeffallan.github.io/claude-skills/skills/workflow/the-fool) - Use before committing to any big decision or architecture choice; challenges thinking from five angles including devil's advocate, red team, and pre-mortem.
- [Web App Testing (official)](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) - Anthropic's official skill for testing web apps inside Claude Code using Playwright; opens a real browser, runs interaction tests, captures screenshots, and reports failures. · 175k stars · updated 2026-09

### Research

- [Claude-Obsidian](https://github.com/AgriciDaniel/claude-obsidian) - Persistent, compounding wiki vault for Claude based on Karpathy's LLM Wiki pattern; use /wiki, /save, and /autoresearch to build a self-updating knowledge base. · 14k stars · MIT · updated 2026-08 · also: [x.com](https://x.com/sourfraser/status/2035454870204100810)
- [Last30days](https://github.com/mvanhorn/last30days-skill) - Researches any topic across Reddit, X, YouTube, HN, and Polymarket from the last 30 days, then synthesizes findings and generates copy-paste prompts; ideal for content and marketing research. Why: Our content research starts here - it is how the guides stay grounded in what people actually struggle with this month. · 61k stars · MIT · updated 2026-09

### Image & Video Editing

- [banana](https://github.com/AgriciDaniel/banana-claude) - Turns Claude into a Nano Banana Pro creative director that writes optimized prompts with Google's 5-component formula and generates or edits images directly via the Gemini API; handles text-to-image, inpainting, style transfer, 4K, and multi-turn creative sessions. (needs a GEMINI_API_KEY · scanned Med Risk) · 1k stars · MIT · updated 2026-08
- [browser-use/video-use](https://github.com/browser-use/video-use) - Agent-native video editing skill for Claude Code that takes raw footage, cuts filler words, color grades, burns subtitles, and produces a final MP4 entirely through natural language instructions. · 24k stars · MIT · updated 2026-08
- [Claude Video Vision](https://github.com/jordanrendric/claude-video-vision) - Gives Claude the ability to watch and understand videos by extracting frames via ffmpeg and processing audio through multimodal backends; ideal for generating creative briefs, hooks, and shot-by-shot breakdowns from any video. · 1.3k stars · MIT · updated 2026-08
- [digitalsamba/claude-code-video-toolkit](https://github.com/digitalsamba/claude-code-video-toolkit) - Full AI-native video production workspace for Claude Code bundling skills, slash commands, templates, and tools covering the entire pipeline from narration and scoring to rendering and composition. · 2.1k stars · MIT · updated 2026-09
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) - Write HTML and CSS to declaratively define animated video frames that render to MP4, purpose-built for AI agents that need to programmatically produce video without a GUI. · 48k stars · Apache-2.0 · updated 2026-09
- [higgsfield-generate](https://github.com/higgsfield-ai/skills) - Gives Claude one-command generation across 30+ models - Nano Banana 2/Pro for images, Seedance 2.0 for video with native audio, plus Kling, Veo, GPT Image 2, 3D, and Marketing Studio - including image-to-video, reframe, and virality scoring. (official Higgsfield · uses your connected Higgsfield MCP/account) Why: Powers our creative AI guides, including the champagne video - one skill instead of five tabs. · 910 stars · MIT · updated 2026-08
- [Nano Banana 2](https://github.com/kingbootoshi/nano-banana-2-skill) - AI image generation skill powered by Gemini 3 Pro; supports green-screen transparency, reference images, and style transfer directly inside Claude Code. · 408 stars · MIT · updated 2026-04
- [Remotion best practices](https://github.com/remotion-dev/skills) - Deep knowledge of animations, timing, and audio sync so Claude can produce programmatic videos using React and Remotion with production-grade output. · 4.5k stars · updated 2026-09
- [seedance-prompt-en](https://github.com/dexhunter/seedance2-skill) - Makes Claude an expert prompt engineer for Seedance 2.0, mastering the @ reference syntax, camera language, beat-matching, and shot structure to turn a rough idea into a precise, production-ready video prompt; built straight from ByteDance's official docs. (no key - pure prompt craft) Why: Pure prompt craft, no API key needed - the difference between a generic clip and a usable shot. · 3.5k stars · MIT · updated 2026-02

### Marketing - Content & Writing

- [Content Research Writer](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/content-research-writer/SKILL.md) - Full research → outline → draft pipeline that adds citations, improves hooks section by section, and enables systematic, high-quality content production at scale. · 74k stars · updated 2026-08
- [Go Viral Bro (GVB)](https://github.com/charlesdove977/goviralbro) - acts as a trainable content brain - it discovers winning topics from 9+ platforms, generates hooks and full scripts, and automatically learns from your analytics to improve your content over time. · 264 stars · MIT · updated 2026-03
- [Humanizer](https://github.com/blader/humanizer) - Claude Code skill that removes signs of AI-generated writing from text. Why: Every piece of copy on agentmatik.ai passes through it. Non-negotiable in our content pipeline. · 45k stars · MIT · updated 2026-09
- [Lookalike content](https://www.linkedin.com/posts/kieranjflanagan_claude-code-is-a-superpower-for-content-creators-ugcPost-7439322613698662401-Kt9I) - Analyzes your past content, identifies the patterns behind what performs best, and uses them to generate new trend-relevant content ideas more likely to resonate with your audience.

### Marketing - Ads & SEO

- [agent-skills/google-ads](https://github.com/itallstartedwithaidea/agent-skills/tree/main/skills/google-ads) - Twelve Google Ads skills covering campaign audits, keyword work, and reporting. · 37 stars · MIT · updated 2026-04
- [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) - Full Meta Ads skill pack that handles competitive intelligence, copy generation, account auditing, and ad scoring. · `npm install -g @anthropic-ai/claude-code` · 9.1k stars · MIT · updated 2026-07
- [ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) - Open-source AI marketing skills - growth experiments, sales pipeline, content ops, outbound, SEO, and finance automation. · 3.5k stars · MIT · updated 2026-09
- [Claude SEO](https://github.com/AgriciDaniel/claude-seo) - Full-site audits, schema validation. 12 sub-skills. · 16k stars · MIT · updated 2026-08
- [ComposioHQ/awesome-claude-skills/competitive-ads-extractor](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/competitive-ads-extractor) - analyzes 3-5 competitors' active ads and outputs a gap analysis showing untapped angles you could own, ranks hooks by frequency, maps offer structures and CTA patterns, and identifies emotional angles nobody in your market is running. · `npx skills add https://github.com/ComposioHQ/awesome-claude-skills/tree/master/competitive-ads-extractor` · 74k stars · updated 2026-08
- [Marketing Skills by Corey Haines](https://github.com/coreyhaines31/marketingskills) - 20+ skills: CRO, copywriting, SEO, email sequences, growth. · 49k stars · MIT · updated 2026-09
- [Marketing skills by Ryze AI](https://github.com/irinabuht12-oss/marketing-skills) - specific but lower quality, 17 free skills that turn Claude into your marketing assistant. · 1.2k stars · updated 2026-09
- [Marketingskills/Ad Creative](https://github.com/coreyhaines31/marketingskills/blob/main/skills/ad-creative/SKILL.md) - Generate on-brand ad creative concepts, copy variations, and visual briefs across channels. · 49k stars · MIT · updated 2026-09
- [Marketingskills/AI SEO](https://github.com/coreyhaines31/marketingskills/tree/main/skills/ai-seo) - Optimize content for AI-powered search engines and answer engines, including structured data, entity coverage, and GEO/AEO best practices. · 49k stars · MIT · updated 2026-09
- [Marketingskills/Content Strategy](https://github.com/coreyhaines31/marketingskills/blob/main/skills/content-strategy/SKILL.md) - Build a full content strategy including pillars, formats, cadence, and distribution channels. · 49k stars · MIT · updated 2026-09
- [Marketingskills/Email Sequence](https://github.com/coreyhaines31/marketingskills/tree/main/skills/emails) - Write multi-step email sequences for onboarding, nurture, and re-engagement campaigns. · 49k stars · MIT · updated 2026-09
- [Marketingskills/Lead Magnets](https://github.com/coreyhaines31/marketingskills/tree/main/skills/lead-magnets) - The lead-magnets skill from Corey Haines' marketing skills collection (the whole collection is listed under Collections). · 49k stars · MIT · updated 2026-09
- [Marketingskills/SEO Audit](https://github.com/coreyhaines31/marketingskills/tree/main/skills/seo-audit) - Run a comprehensive SEO audit covering technical issues, on-page optimization, content gaps, and actionable recommendations. · 49k stars · MIT · updated 2026-09
- [meta-ads-skill](https://github.com/Varnan-Tech/opendirectory/blob/main/skills/meta-ads-skill) - Use when interacting with the Meta Ads CLI to manage accounts, campaigns, ads, and insights. Act as an Expert Media Buyer. · 636 stars · MIT · updated 2026-08
- [noise-to-linkedin-carousel](https://github.com/Varnan-Tech/opendirectory/blob/main/skills/noise-to-linkedin-carousel) - Transforms messy, unstructured source material (transcripts, rough notes, voice memos) into polished, formatted LinkedIn carousel posts ready to publish. · 636 stars · MIT · updated 2026-08

## Collections

Lists and directories I go back to when I need something I do not have yet.

- [awesome claude code](https://github.com/hesreallyhim/awesome-claude-code) - A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. · 53k stars · updated 2026-09
- [awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) - A curated GitHub list maintained by the community. Great if you prefer a simple, hand-picked list over a full marketplace. · 10k stars · updated 2026-08
- [claude code best practice](https://github.com/shanraisshan/claude-code-best-practice) - from vibe coding to agentic engineering - practice makes claude perfect. · 65k stars · MIT · updated 2026-09
- [opendirectory](https://github.com/Varnan-Tech/opendirectory) - AI Agent Skills built for GTM, Technical Marketing, and growth automation. · 636 stars · MIT · updated 2026-08
- [Skills Guide | Claude Skills](https://jeffallan.github.io/claude-skills/skills-guide) - Decision trees and skill combinations for choosing the right skill.
- [gstack](https://github.com/garrytan/gstack) - my notes on it; the entry itself is under Agent teams and subagents:
  - **The core idea**
  - gstack is a process, not a toolbox - its skills mirror a sprint: Think → Plan → Build → Review → Test → Ship → Reflect. Each skill writes an artifact the next one reads (/office-hours writes a design doc that /plan-ceo-review reads; /plan-eng-review writes a test plan that /qa picks up). So order matters more than which individual command you run.
  - **The main loop (in order)**
  - 1. /office-hours - start every new idea here. You describe what you want to build; it interrogates you with forcing questions, pushes back on your framing, and produces a design doc. Why first: it reframes the problem before any code exists, and the design doc feeds everything downstream.
  - 2. /autoplan - turn the idea into a reviewed plan. One command that automatically runs the CEO review (scope: is this the right thing?), design review, eng review (architecture, edge cases, tests), and DX review - auto-deciding the obvious calls and only surfacing taste decisions to you. Use this instead of running /plan-ceo-review, /plan-eng-review, /plan-design-review individually unless you want one specific lens.
  - 3. Build - normal Claude Code work, implementing the approved plan.
  - 4. /review - before any PR. Staff-engineer-style review hunting for bugs that pass CI but break in production. Auto-fixes the obvious, asks you about the risky ones.
  - 5. /qa &lt;url> - test it for real. Opens an actual headless Chromium browser, clicks through your flows, finds bugs, fixes them with atomic commits, and generates regression tests. /qa-only does the same but report-only (no code changes). /setup-browser-cookies first if the page needs auth.
  - 6. /ship - open the PR. Syncs main, runs tests, audits coverage, pushes, opens the PR. Then /land-and-deploy merges, waits for CI/deploy, and verifies production. /canary watches production afterwards for console errors and regressions.
  - 7. /retro - weekly. Reviews what shipped, test health trends, and growth opportunities across the week.
  - **Picking the right review**
  - **You built... | Before code | After shipping**
  - UI / web app | /plan-design-review | /design-review
  - API / CLI / docs | /plan-devex-review | /devex-review
  - Architecture / perf | /plan-eng-review | /review
  - Everything | /autoplan | (none)
  - **Standalone tools worth knowing**
  - /investigate - systematic root-cause debugging with a hard rule: no fixes without investigation first. Use this instead of "just try a fix" when something breaks.
  - /cso - OWASP Top 10 + STRIDE security audit with a high confidence gate (low noise). Good before exposing anything publicly.
  - /browse - the headless browser directly (~100ms per command); this is what /qa uses under the hood.
  - /design-shotgun → /design-html - generates 4-6 mockup variants in a comparison board, learns your taste from feedback, then converts the winner into production HTML.
  - /careful / /freeze / /guard - session guardrails: block destructive commands or restrict edits to one directory.
  - /learn - manage what gstack remembers about your codebase across sessions.
  - /gstack-upgrade - keep it current.
  - **Minimal first run (the README's own suggestion)**
  - /office-hours - describe something you're building (e.g. one of your client web apps)
  - /plan-ceo-review on the resulting idea
  - /review on any branch with changes
  - /qa on a staging URL
  - That's enough to know whether the full sprint loop is for you.

## Field notes

Working rules I keep in Notion and refine as Claude Code changes - CLAUDE.md, context, hooks, structure, effort.

### General best practices

- [Dave Killeen - Running a whole day out of Claude Code](https://www.linkedin.com/posts/aagupta_dave-killeen-cant-write-code-he-runs-his-share-7440767281930067968-AHA3) - Field CPO at Pendo uses Claude Code for daily planning, backlog management, and career tracking - a practical model for non-engineers using CC as a full personal operating system.
- [What 5 months of nonstop Claude Code taught me](https://www.reddit.com/r/ClaudeAI/comments/1r6cn6t/what_5_months_of_nonstop_claude_code_taught_me) - Practitioner breakdown of hard-won lessons from sustained daily use: what actually works, what breaks down at scale, and the habits that compound over time.
- weekly review of all skills and claude code files

### Plan vs bypass mode

- with plan mode significantly better output, more information in plan mode = better input = better output (shift + tab twice to enter plan mode)
- before asking to build a feature, think about the architecture
- before asking to debug, think about what you actually know about the problem
- before asking to refactor something, think about what the end state should look like
- deep back and forth with ChatGPT/Gemini/Claude, defining what I want to build, ask the LLM for the various options you can take in terms of system design, settle on a solution. asking each other questions, not just a one way street.
  - **Plan mode examples**
    - Architecture might be wrong (Wait... this should maybe be modularized, Maybe this should be two workflows, What if this scales?)
    - Adding a New Feature Mid-Build (Where does retry sit? Is it workflow-level or node-level? Do we centralize error handling?)
    - Need Clarification / Edge Case Thinking
      - What if the webhook fails?
      - What if OpenAI times out?
      - What if the transcript is empty?
      - What if 5 jobs hit simultaneously?
    - Want to refactor cleanly
      - Review this workflow as a senior automation engineer and suggest structural improvements before modifying anything.

### Effort

- Default changed (March 2026): Pro/Max plans now default to medium, not high. Fix: export CLAUDE_CODE_EFFORT_LEVEL=high in your shell profile
- 4 levels - Low (skip thinking, fast/cheap) → Medium (balanced, good default for implementation) → High (always thinks, proactive file reading) → Max (no ceiling, Opus only, expensive)
- The pattern: Plan/architecture = High + Opus → Implementation = Medium + Sonnet → Stuck after 2 attempts = Max
- Adaptive thinking already self-regulates within a level - Claude skips deep thinking on trivial tasks at medium. You're only setting the ceiling, not forcing it on every prompt
- Cost: Max can be 10x more tokens than Low on the same prompt. Opus 4.6 uses ~6-8% of subscription quota per heavy prompt
- Switch mid-session with /effort high or /effort medium - build the habit at the start of planning vs execution blocks
- Most reliable way to set Max: CLAUDE_CODE_EFFORT_LEVEL=max env var - effortLevel: "max" in settings.json gets silently overwritten by the UI (known bug)
- Ultrathink keyword ≠ Max - it actually triggers High. Use /effort max explicitly if you want true max
- opusplan model alias - automatically uses Opus for planning, Sonnet for execution. Best of both worlds for full sessions
- Skill YAML frontmatter supports effort: low - useful for batch/automation skills so they don't burn quota
- use medium for implementation, high for complex reasoning, and max when you're stuck or the stakes are high. The effort parameter controls far more than thinking depth - it governs tool-call appetite, file-reading behavior, and response length simultaneously

### Prompting basics

- give it full execution loop = faster - “write, run tests, fix failures”
- Break every task into smaller checkpoints - "Create login route, then session handling.", Smaller scope = better output
- plan mode - architect mode, whiteboard mode, system design thinking, claude does not execute and call tools, thinks through structure, risks, dependencies, proposes clear plan before touching any system
- bypass permissions - builder mode, direct system manipulation, Claude does not have to ask anything
- can switch from bypass back to plan mode to rebuild architecture, adding new feature, need clarification/edge case thinking/want to refactor cleanly
- potential flow - 🧠 Plan,⚡ Build, 🧠 Re-evaluate, ⚡ Refine, 🧠 Scale-thinking, ⚡ Optimize implementation

### Structure

- Run /init on every project - Claude scans your codebase and creates a CLAUDE.md rules file, review it, edit it, make it yours.
- Lazy loading is what makes one big workspace free - subfolder CLAUDE.md files load ONLY when Claude touches files in that subtree. Workspace size does not equal context size - the entire argument against a monorepo dies here.
- Memory files concatenate, they never override - the popular 'deeper CLAUDE.md wins on conflict' claim is wrong per official docs. Contradicting instructions between root and subfolder = coin-flip behavior. Nested files must add, not contradict.
- The launch directory IS the scope - .mcp.json and .claude/settings.json load only from where you start Claude - they are NOT inherited from parents. cd marketing && claude = marketing MCP servers + skills without the n8n stack. This one habit replaces the entire reason people keep separate repos.
- Nested skills are directory-scoped, not session-scoped - a .claude/skills/ inside a subfolder activates whenever Claude works there, even in a session started at root.
- Three-boundary test for a separate repo - only lifecycle (deploys independently), audience (others push to it), or access (NDA/privacy) justify a repo. Notes, plans, client working files, scripts - all in the one workspace.
- Per-role repos fail empirically - the role you do 90% of the time absorbs everything; the other repos die. Real case: 6 role repos dead for 2+ months, backups silently stale, real work stranded in one of them.
- Root CLAUDE.md = map, not manual - folder table + global rules + pointers, under 200 lines (official guidance). Update it when the SYSTEM changes, not when the work changes. Detail goes in domain files and skills.
- Exported configs are the leak vector - n8n workflow JSONs, notebook outputs, API dumps carry live tokens into git - not your source code. A gitleaks pre-commit found 16 live secrets in one workspace. .mcp.json takes ${ENV_VAR} refs, never literals.
- Old repo histories are radioactive - when consolidating, rsync content-only and never merge git history that ever held a secret - then rotate those keys. Archive the old repo on GitHub instead of deleting: free, reversible.
- Worktrees hide real work - before deleting any repo, check .claude/worktrees/ - files can exist ONLY there, one prune away from loss. Real case: 44 production skills lived solely inside an uncommitted worktree.
- Transcripts are plaintext - everything Claude reads can land in ~/.claude/projects/. A root session can read every client folder - NDA or competing clients need their own repo (or devcontainer), not a subfolder.
- Scaffolding rots - elaborate .claude/ rule/command/agent trees built up front decay - one practitioner deleted 60% within 4 months. Add structure only when a pain repeats.

### CLAUDE.md

- **A version from AI with Remy**
  - Plan mode as the default. For anything non-trivial (3+ steps or an architectural call), Claude plans before building. If something goes sideways mid-task, it stops and re-plans instead of pushing through. Kills the "Claude runs off and does the wrong thing" risk before it starts.
  - Subagent-first orchestration. The main context window is sacred. It's for decisions and talking to me. Anything grunt work (reading 3+ files, broad searches, running tests, producing intermediate analysis) gets delegated to subagents, and their results flow back as summaries, not raw output. This is the single biggest unlock for long-session work, because it stops the main context from getting polluted with tool output.
  - Obsidian as the second brain. My vault is the single source of truth for every bit of business context (brand guidelines, strategy docs, meeting notes, client info, decisions). Every workspace loads the relevant bits via @imports at session start, so context flows in automatically.
  - Verification before done. Nothing is complete until it's proven to work. Run the tests, check the logs, demonstrate correctness. "Would a staff engineer approve this?" is the internal check before anything gets marked done. Kills the "ship it and see" instinct.
  - Boil the Ocean. The standard isn't "good enough," it's "holy shit, that's done." Stole this from Garry Tan
- system prompt for a project, reads before each answer
- Routing file - CLAUDE.md should be a routing file, not a knowledge dump. Keep it under 150 lines. Point to .claude/rules/\*.md for detailed specs and docs/ for architecture. Otherwise it gets so long that Claude skims it and misses the important stuff.
- auto-compaction - at ~83.5% of the 200K token window - is identified as the single highest-leverage skill for effective usage
- folder structure and where it finds files, frameworks we are using, what end goal is
- Build a validation loop - Build, test, compile commands inside CLAUDE.md. Claude self-corrects when it can validate its own output. Without this, it hallucinates fixes.
- Never manually edit rules - "Update the rules so we never do this again." One sentence. Claude maintains its own CLAUDE.md
- update constantly - update CLAUDE.md every time the CC makes a mistake
- press the # key while working - will add instructions to your CLAUDE.md automatically
- /init - go through everything we have done and then CC would create CLAUDE.md file
- keep under 200 lines and only important information/context, bloats your context window, only add what's unique to a project.
- project-specific (everything part of the flow, specific/weird stuff) + include reason behind instruction (use x because we had production bugs from x)
  - **CLAUDE.md based on best practice from Boris Cherny**
    - → Workflow Orchestration: Mandates "Plan Node Default" for any task over 3 steps. Uses subagents liberally to keep the main context window clean.
    - → Self-Improvement Loop: This is the real magic. After ANY correction, it updates a tasks/lessons .md file. You're building a compounding system where the mistake rate drops over time because it actively learns from your feedback.
    - → Verification Before Done: Can't mark a task complete without proving it works. Diffs behavior. Runs tests. Checks logs. The bar? "Would a staff engineer approve this?"
    - → Autonomous Bug Fixing: Zero hand-holding. Point it at failing CI tests or error logs... it just goes to work. No constant context switching from you.
    - → Strict Task Management: Forces a "Plan First" approach written to a todo .md with checkable items before any implementation starts.
    - And perhaps the most important part?
    - It forces the AI to prioritize simplicity, find root causes instead of temporary fixes, and minimize the blast radius of every change. Senior developer standards. Not shortcuts.

### Security and passwords

- keep secrets in 1Password for portability, and also maintain project-specific .env organization

### Context

- [claude-supermemory](https://github.com/supermemoryai/claude-supermemory) - Enable Claude Code to learn in real-time, update it's knowledge, and grow with you, using supermemory. · 2.8k stars · updated 2026-09
- /clear between features - Old context contaminates new tasks. One feature per session. Start clean or pay the token tax.
- Audit with /context regularly - MCPs destroy your token budget. /context shows the biggest offenders. Disable what you don't need. Most engineers never check this.
- Compact aggressively (~50%) for multi-file coding; for linear work and workflows only when CC starts forgetting and repeating mistakes
- at 20-40% context usage quality of the output starts to chip away, once dropping more context makes it worse, not better
- scope conversations - one conversation per feature or task
- Use external memory - complex = Claude write plans and progress to actual files ( SCRATCHPAD.md or plan.md), persist across sessions, if hierarchy system of files = keep on top
- copy-paste reset - context bloated > copy everything from terminal > run /compact to get summary, /clear the context and start fresh

### Hooks

- [Notifications](https://www.aitmpl.com/component/hook/automation/simple-notifications) - sound notification once a task is done.
- use hooks (not CLAUDE.md) for enforcement since instructions get "forgotten" in long context
- leverage anti-rationalization Stop hooks to prevent Claude from rationalizing incomplete work

### Personal assistant

- [How I structure Claude Code projects (Reddit post)](https://www.reddit.com/r/ClaudeAI/comments/1r66oo0/how_i_structure_claude_code_projects_claudemd) - Reddit post on splitting memory into .claude/rules files, a Stop hook that captures lessons as you go, and CLAUDE.md as a routing file - my notes on it are below.
  - Instead of one big CLAUDE.md, I split into .claude/rules/memory-\*.md files - profile (facts about me), preferences (how I like things done), decisions (past choices for consistency), and sessions (rolling summary of recent work). Claude Code auto-loads everything in .claude/rules/ so it's always in context without bloating the main CLAUDE.md.
  - Enforcement: CLAUDE.md has a MANDATORY section telling Claude to update memory files as it goes, not at the end. The problem is Claude "forgets" instructions mid-session, so I added a Stop hook that checks if learning-likely files changed and reminds to capture anything new. Belt and suspenders.
    ```text
    ### Auto-Update Memory (MANDATORY)

    **Update memory files AS YOU GO, not at the end.** When you learn something new, update immediately.

    | Trigger | Action |
    |---------|--------|
    | User shares a fact about themselves | → Update `memory-profile.md` |
    | User states a preference | → Update `memory-preferences.md` |
    | A decision is made | → Update `memory-decisions.md` with date |
    | Completing substantive work | → Add to `memory-sessions.md` |

    **Skip:** Quick factual questions, trivial tasks with no new info.

    **DO NOT ASK. Just update the files when you learn something.**
    ```
  - The key lines are "AS YOU GO, not at the end" and "DO NOT ASK." Without both of those it tends to either forget or ask permission every time.
  - 2. Stop hook (settings.json → hooks.Stop):
    ```text
    #!/bin/bash
    CONTEXT=$(cat)

    STRONG_PATTERNS="fixed|workaround|gotcha|that's wrong|check again|we already|should have|discovered|realized|turns out"
    WEAK_PATTERNS="error|bug|issue|problem|fail"

    if echo "$CONTEXT" | grep -qiE "$STRONG_PATTERNS"; then
    cat << 'EOF'
    {
    "decision": "approve",
    "systemMessage": "This session involved fixes or discoveries. Consider running /reflect to capture learnings in project docs."
    }
    EOF
    elif echo "$CONTEXT" | grep -qiE "$WEAK_PATTERNS"; then
    echo '{"decision":"approve","systemMessage":"If you learned something non-obvious this session, run /reflect to update docs."}'
    else
    echo '{"decision": "approve"}'
    fi
    ```
  - This runs when a session ends. It pattern-matches the conversation for signals that learning happened (corrections, discoveries, workarounds) and nudges Claude to write them down. It's a safety net - the CLAUDE.md instruction handles ~90% of it, but the hook catches sessions where it forgot.
  - The memory files themselves live in .claude/rules/ so they're auto-loaded as context every session. No RAG, no embeddings - just flat markdown files that Claude reads on startup and edits in-place.
- **MCP - connecting tools**
  - MCP: Biggest unlock for me was connecting tools that Claude can't reach natively. Browser automation for research, Google Workspace for email/calendar, Reddit for monitoring - turns Claude Code from a coding tool into an actual assistant.
- **CLAUDE.md as routing file**
  - The thing most people miss: CLAUDE.md should be a routing file, not a knowledge dump. Keep it under 150 lines. Point to .claude/rules/\*.md for detailed specs and docs/ for architecture. Otherwise it gets so long that Claude skims it and misses the important stuff.

## Tools and memory

Memory plugins, usage meters and small utilities around Claude Code.

- [anthropics/claude-code](https://github.com/anthropics/claude-code) - Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through... · 144k stars · updated 2026-09
- [CodexBar](https://github.com/steipete/CodexBar) - macOS menu bar usage app - Show usage stats for OpenAI Codex and Claude Code, without having to login. · 21k stars · MIT · updated 2026-09
- [Ollama + Claude Code = 99% CHEAPER](https://www.youtube.com/watch?v=O2k_qwZA8HU) - Running locally with local model or Openrouter.
- [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) - #1 Persistent memory for AI coding agents based on real-world benchmarks. · 28k stars · Apache-2.0 · updated 2026-09
- [Usage for Claude](https://apps.apple.com/us/app/usage-for-claude/id6755173244) - macOS menu bar app that shows your Claude usage, from the App Store.

## n8n with Claude Code

Building n8n workflows from Claude Code - the MCP server and skills that make it work.

- [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) - n8n-MCP: A Model Context Protocol (MCP) server that gives Claude Code deep, structured access to n8n's vast library of workflow automation nodes, properties, operations, and documentation. · 22k stars · MIT · updated 2026-09
- [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) - n8n skillset for Claude Code to build flawless n8n workflows. · 6.2k stars · MIT · updated 2026-09 · also: [skills.sh](https://skills.sh/czlonkowski/n8n-skills)

## Other useful lists

This list is deliberately short and opinionated. When you want the exhaustive version, these are the ones I actually open:

- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - the reference directory for Claude Code itself: slash commands, hooks, status lines, tooling, plugins. Generated from a curated CSV, so it stays consistent. Go here when you want everything that exists, not just what one person kept.
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) - skills as a category, with the skill folders committed in the repo so you can read a SKILL.md before installing it. Useful for seeing how other people structure a skill.
- [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) - a large catalogue of subagent definitions by domain. Worth a skim when you are designing an agent team and want prior art for the role split.

The difference is intent, not quality: those are directories of what exists, this is a record of what I kept after using it. If a link appears in both, theirs will be more complete and mine will tell you whether it survived contact with real work.

## How this list is built

The source is a private Notion page where I keep notes while I work. A sync script in my workspace (`awesome-sync.py`, not in this repo) reads that page through the Notion API and keeps only the sections that are explicitly mapped as public - everything else stays private by default. It canonicalizes every URL (https only, tracking parameters dropped, `youtu.be` and `twitter.com` rewritten), drops links to private places (Notion, Google Drive, course platforms), scans every string for secrets and private names, and writes three files: `data/links.csv` (one row per link), `data/notes.json` (the field notes) and `data/_report.md` (what was excluded and why).

From there everything is automated and reproducible from this repo alone:

- `tools/enrich.py` checks every link and writes `data/enrichment.json`: stars, license, last push and archive state from the GitHub API (renamed repositories are followed), titles from YouTube and X oEmbed, and a plain HTTP check with a browser user agent for everything else.
- `tools/build.py` renders this README from `data/` + `config/sections.json` + `templates/README.template.md`. Entries are sorted by name inside each section; the build is deterministic, so running it twice produces the same file.
- `tools/lint.py` fails on dead links, descriptions under 30 characters, duplicate names or URLs, non-https links, tracking parameters, links to private hosts, long dashes, placeholders, thin sections and broken table-of-contents anchors. Whatever it cannot fix on its own is listed under "Open decisions" in `data/_report.md`.
- A weekly GitHub Action (`.github/workflows/links.yml`) re-runs the checks and opens a pull request when the README changes. `data/_dead.md` lists what needs a human look.

Nothing in this README is edited by hand. Fixes go to `data/overrides.json` (keyed by the entry id in `data/links.csv`) and the next build picks them up.

Current build: 135 entries in 8 sections, 139 field notes. Links checked: 135, dead: 0, last check: 2026-09-09. What the sync excluded and why is in `data/_report.md`.

## License

The content of this list (README and the files in `data/`) is licensed under [CC BY 4.0](LICENSE) - share and adapt it with attribution. The scripts in `tools/` are MIT licensed ([LICENSE-CODE](LICENSE-CODE)).
