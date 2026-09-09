# awesome-sync report

Source page: `2f6daecfce6b80088d45ca8548bba01b` - generated 2026-09-09. Block ids are Notion block ids (open the page and append `#<id without dashes>` to jump).

## Counts

- entries: 135
  - Agent teams and subagents: 3
  - Collections: 5
  - Field notes / Context: 1
  - Field notes / General best practices: 2
  - Field notes / Hooks: 1
  - Field notes / Personal assistant: 1
  - Learn: 12
  - Prompting: 5
  - Skills / Development: 15
  - Skills / General: 11
  - Skills / Image & Video Editing: 9
  - Skills / Marketing - Ads & SEO: 15
  - Skills / Marketing - Content & Writing: 4
  - Skills / Project management: 1
  - Skills / Research: 2
  - Skills / Token burn & models: 5
  - Skills / Webdesign MCP & UI elements: 3
  - Skills / Webdesign dev skills: 16
  - Skills / Webdesign taste skills: 17
  - Tools and memory: 5
  - n8n with Claude Code: 2
- notes: 152
- media/file blocks skipped: 37

## Mapped toggles

- `Learning` -> links -> Learn
- `Agent Teams & Sub-agents (+gstack)` -> links+notes -> Agent teams and subagents
- `Prompting Fable 5` -> notes -> Prompting
- `Skills` -> links -> Skills
- `Skills > General` -> links -> Skills / General
- `Skills > Token burn & models` -> links -> Skills / Token burn & models
- `Skills > Webdesign taste skills` -> links -> Skills / Webdesign taste skills
- `Skills > Webdesign dev skills` -> links -> Skills / Webdesign dev skills
- `Skills > Webdesign MCP & UI elements skills` -> links -> Skills / Webdesign MCP & UI elements
- `Skills > Project management` -> links -> Skills / Project management
- `Skills > Development` -> links -> Skills / Development
- `Skills > Research` -> links -> Skills / Research
- `Skills > Image & Video, Editing` -> links -> Skills / Image & Video Editing
- `Skills > Marketing - Content & Writing` -> links -> Skills / Marketing - Content & Writing
- `Skills > Marketing - Ads & SEO` -> links-only-github -> Skills / Marketing - Ads & SEO
- `Skills > GTM & Sales` -> private -> 
- `Skills > N8N` -> private -> 
- `Skills > Reviewing skills` -> private -> 
- `Skills > Collections` -> private -> 
- `Collections` -> links+notes -> Collections
- `Collections > gstack - Use Garry Tan's exact Claude Code setup: ` -> links+notes -> Collections
- `General best practices` -> links+notes -> Field notes / General best practices
- `General best practices > Plan vs Bypass mode` -> links+notes -> Field notes / Plan vs bypass mode
- `General best practices > Effort` -> links+notes -> Field notes / Effort
- `Prompting` -> links+notes -> Field notes / Prompting basics
- `Prompting > Effort` -> links+notes -> Field notes / Effort
- `Looping` -> links -> Learn
- `Structure` -> links+notes -> Field notes / Structure
- `Memory` -> links -> Tools and memory
- `Install Context7 MCP for docu` -> links -> Tools and memory
- `CLAUDE.md` -> links+notes -> Field notes / CLAUDE.md
- `Security & Passwords` -> notes -> Field notes / Security and passwords
- `Optimizing Token Burn` -> links -> Tools and memory
- `Context` -> links+notes -> Field notes / Context
- `Prompts` -> links -> Prompting
- `Hooks` -> links+notes -> Field notes / Hooks
- `Personal assistant` -> links+notes -> Field notes / Personal assistant
- `Useful tools` -> links -> Tools and memory
- `N8N` -> links -> n8n with Claude Code
- `Vibing videos (Comfy UI)` -> private -> 
- `Visual guides` -> private -> 

## Mapping decisions recorded in the config

- `Prompting Fable 5` -> notes: Matt's own prompt patterns - publishable as notes.
- `Skills` -> links: Root toggle only holds sub-toggles; each one is mapped below. Anything added later inherits 'links' - list it here first.
- `Skills > Marketing - Ads & SEO` -> links-only-github: Nested toggles embed paid course lesson text (NoeAI classroom): only github URLs survive and prose is read only from the toggle's direct children.
- `Skills > GTM & Sales` -> private: Not in the publishing brief - Matt's decision (4 GTM skill links).
- `Skills > N8N` -> private: Not in the publishing brief - Matt's decision (official n8n-io/skills link; would fit 'n8n with Claude Code').
- `Skills > Reviewing skills` -> private: Empty toggle.
- `Skills > Collections` -> private: Not in the publishing brief - Matt's decision (skill collections incl. tenfoldmarc reviews; overlaps the top-level Collections toggle).
- `Collections > gstack - Use Garry Tan's exact Claude Code setup` -> links+notes: Explicit for transparency - same as inherited. Matt's walkthrough of the gstack loop becomes notes under the gstack entry.
- `Prompting` -> links+notes: Subsection named 'Prompting basics' so it does not collide with the 'Prompting' section (Fable 5 patterns) in README anchors.
- `N8N > Provide N8N server url & API` -> private: Holds a live instance URL and API key. Forced private here AND in private_block_ids; the run prints ROTATE for the key block.
- `Visual guides` -> private: Image blocks only.

## Open questions recorded in the config (need Matt's decision)

- Skills > GTM & Sales (4 links), Skills > N8N (the official n8n-io/skills link - mapping it into 'n8n with Claude Code' would also lift that section above the 3-item minimum) and Skills > Collections (tenfoldmarc's reviewed skills, two threads) are private only because the publishing brief did not list them - map them if they should be public.
- Six entries exist only on agentmatik.ai/llms-full.txt; three of them are OpenClaw-only, not Claude Code (antfarm, qmd-skill, openclaw-supermemory) - keep them, or add their repo URLs to exclude_urls.
- Tools and memory > anthropics/claude-code comes from the toggle 'Install Context7 MCP for docu', which links the Claude Code repository rather than Context7 - relink in Notion (github.com/upstash/context7) or drop the toggle.
- Token burn & models > Omniroute is still listed in Notion although the workspace assessment concluded it is not worth installing - keep or remove at the source.
- agentmatik.ai/llms-full.txt links emil-design-eng to github.com/emilkowalski/skill (the repository is now /skills); the sync follows the redirect, but the site should be corrected.
- Two links are gone for good: the RoundtableSpace X post (deleted) and iamzhihuix/happy-claude-skills (repository removed, no fork found) - remove them in Notion or set a new url in data/overrides.json. The @youraicompass SEO prompts Instagram post is gone too (2026-09-09); the 5 prompt names Matt saved under it are sub-toggles that the links-mode Prompts toggle does not publish - turn them into notes if they should go public.
- Social sources (Instagram carousels, the Threads post, X posts and X articles) were described in Notion on 2026-09-09 from the actual post content (Apify scrapes, slides read one by one); link_mention spans had to be rewritten as plain text links because the Notion API refuses to write link_mention objects back.

## Unmapped, defaulted to private (fail closed)

Toggles:
- `Skills > Collections > tenfoldmarc's GitHub (recommended first)` (35fdaecf-ce6b-80b3-9bb0-e5899213a68b)
- `Skills > Collections > Dipanshu Kushwaha - Relevant Claude Code Skills - Curated th` (3a9daecf-ce6b-8057-8207-ff849b9442af)

Child pages (always private):
- My CC Setup (383daecf-ce6b-80f1-af99-f22ad8409a62)
- Used Hooks (399daecf-ce6b-80ce-a381-cf8cb5e13d5c)
- Commands (317daecf-ce6b-80f6-a769-d6929927eeb4)
- Working in CC system (364daecf-ce6b-807d-b2f3-d45adb0e59df)
- Optimization (341daecf-ce6b-8008-a2c9-f2086d2a1e4e)

Child databases (always private):
- none

Loose root blocks (private):
- column (364daecf-ce6b-8070-8be9-d9ed10e4c816)
- paragraph (39bdaecf-ce6b-801a-8366-f589164b258a)
- paragraph (39bdaecf-ce6b-80a0-af3f-c8aead43ea5c)
- column (364daecf-ce6b-8058-bcf4-d14c385b7f4c)
- column (364daecf-ce6b-80a8-a3b7-cea6ebd25e70)
- bulleted_list_item (32fdaecf-ce6b-801e-abf3-e4cf2a14a0c6)
- bulleted_list_item (32fdaecf-ce6b-8037-98f0-fe828a7a9da1)
- bulleted_list_item (32fdaecf-ce6b-80b3-a2ff-ecf6cd1cea4e)
- bulleted_list_item (361daecf-ce6b-803e-b284-c88a88481d8c)
- paragraph (385daecf-ce6b-8037-8893-f9203b6fdca5) - github.com
- bulleted_list_item (33adaecf-ce6b-802a-bb52-f575257148fe)
- bulleted_list_item (3a9daecf-ce6b-8015-af6c-f6383b8b20d0)
- bulleted_list_item (345daecf-ce6b-80ec-878d-d3afba3eb894)
- bulleted_list_item (345daecf-ce6b-80e6-965a-c533a9d1e31a)
- bulleted_list_item (32fdaecf-ce6b-8071-9f1e-f90806202a29)
- bulleted_list_item (33adaecf-ce6b-8030-8453-cddb530ca6eb)
- bulleted_list_item (33ddaecf-ce6b-8083-a7c2-fcbda710f2e3)
- bulleted_list_item (33cdaecf-ce6b-805f-a7d8-eefb359c819e)
- bulleted_list_item (32fdaecf-ce6b-809a-9de2-f5e2b5973cab)
- bulleted_list_item (32fdaecf-ce6b-804b-9e28-fc0190d94aec)
- bulleted_list_item (33adaecf-ce6b-80ec-8ae1-c96886f54968)
- bulleted_list_item (458267e5-9952-472d-8b6c-4508fee1c9aa)
- bulleted_list_item (cdbb7e58-764a-40cc-8227-7d1263afa5f4)
- heading_2 (35fdaecf-ce6b-80fd-8e37-f5f3edbc29a2)
- bulleted_list_item (35fdaecf-ce6b-8030-abb7-c4a6c6f564e2)
- bulleted_list_item (35fdaecf-ce6b-8048-a31f-feee290b3e34)
- bulleted_list_item (35fdaecf-ce6b-80ef-a931-ca053b7b927f)
- bulleted_list_item (35fdaecf-ce6b-8018-b83a-f101099d9993)
- bulleted_list_item (35fdaecf-ce6b-805d-98b1-d41c0bb3b8e3)
- bulleted_list_item (35fdaecf-ce6b-808a-9392-c61a277dd668)
- bulleted_list_item (35fdaecf-ce6b-80a7-b142-f2392e89f016)
- bulleted_list_item (35fdaecf-ce6b-80dc-a93d-ebc4ae636e4e)
- bulleted_list_item (35fdaecf-ce6b-804b-b608-f128e1fdf9c9)
- heading_2 (35fdaecf-ce6b-8067-82aa-caeb41e4fadf)
- bulleted_list_item (35fdaecf-ce6b-80f6-ae41-d00c4bf0e3e2)
- bulleted_list_item (35fdaecf-ce6b-80e7-b40d-e06b75ca4eb3)
- bulleted_list_item (35fdaecf-ce6b-80a9-9e72-e690009163ae)
- bulleted_list_item (35fdaecf-ce6b-809e-9bd5-d2027f48d8ff)
- bulleted_list_item (35fdaecf-ce6b-8057-866c-e70e1f5f313b)
- bulleted_list_item (35fdaecf-ce6b-80ec-92b6-e1dbcbc6dc56)
- bulleted_list_item (35fdaecf-ce6b-809e-be55-eb2062ec6f70)
- heading_2 (35fdaecf-ce6b-80b5-a104-e0a4af18416c)
- bulleted_list_item (35fdaecf-ce6b-8093-af7b-f566a46bbb01)
- bulleted_list_item (35fdaecf-ce6b-8094-af41-c43a0698d745)
- heading_2 (35fdaecf-ce6b-80ac-bb37-eef31dca7890)
- bulleted_list_item (35fdaecf-ce6b-809b-b3c7-cb3f207425de)
- bulleted_list_item (35fdaecf-ce6b-80b0-96f4-e04792748eef)
- bulleted_list_item (35fdaecf-ce6b-8016-9b38-fdb4f677f2c8)
- bulleted_list_item (35fdaecf-ce6b-8025-a78c-e79442160642)
- bulleted_list_item (35fdaecf-ce6b-80b3-92f4-f035f908270d)
- heading_2 (35fdaecf-ce6b-805d-8605-e49fd5d25da6)
- bulleted_list_item (35fdaecf-ce6b-80fe-b58c-d256a44aa0c9)
- bulleted_list_item (35fdaecf-ce6b-8048-8078-f56795c00c6f)
- bulleted_list_item (35fdaecf-ce6b-805c-9612-da635dba438f)
- bulleted_list_item (35fdaecf-ce6b-808e-b86b-d91cd503d7a4)
- bulleted_list_item (35fdaecf-ce6b-80b4-a419-e43b0455efed)
- bulleted_list_item (35fdaecf-ce6b-80ca-988b-c300d17eb042)
- bulleted_list_item (35fdaecf-ce6b-80e7-995c-d1cedc082f86)
- bulleted_list_item (35fdaecf-ce6b-80a7-ba45-e5eddf6f57e6)
- bulleted_list_item (3a9daecf-ce6b-80b1-85e1-ef835c265ace)
- bulleted_list_item (3a9daecf-ce6b-80b0-b5af-f86851272e32)
- column_list (32cdaecf-ce6b-8023-848c-ccbb397ddd19)
- column (32cdaecf-ce6b-8036-86bc-fcc374d01725)
- column (32cdaecf-ce6b-806a-87f9-da9a085d5748)
- column (32cdaecf-ce6b-8088-b40e-d968eb89b232)
- paragraph (32cdaecf-ce6b-80b7-b64c-f11830c11bf9)
- paragraph (32cdaecf-ce6b-80ee-a50c-e74fcafe782d)

Blocks forced private by config (private_block_ids):
- column_list (364daecf-ce6b-80f8-ae05-ccd23a158bc2)
- paragraph (37cdaecf-ce6b-8014-b1ec-d0418471f8f5) - One note for your setup: the heavyweight flow (office-hours 
- bulleted_list_item (395daecf-ce6b-8177-a565-dce2faa7358d) - Full playbook - guides/claude-code-workspace-structure-playb
- toggle (31bdaecf-ce6b-8050-84e5-cd86b2788f95) - Provide N8N server url & API
- paragraph (31bdaecf-ce6b-807c-ae07-c6a30bfccd05)
- paragraph (31bdaecf-ce6b-8044-980e-e686b717519d)
- bookmark (35fdaecf-ce6b-80de-8bf1-c829c8e15a00)
- file (340daecf-ce6b-8050-ade8-d030f9da7e6c)
- child_page (fa3daecf-ce6b-8247-9e47-011b791916e0)
- paragraph (32cdaecf-ce6b-801e-9241-c644683ce723)
- paragraph (394daecf-ce6b-8075-9da8-fd30aefd2bee)
- paragraph (32cdaecf-ce6b-80f9-a709-cdb4909ec087)
- child_page (335daecf-ce6b-805a-99c8-eb2fe25f3713)
- child_page (339daecf-ce6b-8115-968a-c787f65159a7)
- child_page (367daecf-ce6b-81cf-8a67-fe18aa72eafd)
- child_page (3b4daecf-ce6b-81f1-8cc2-e597203b0bc1)
- child_database (3d3daecf-ce6b-8139-a5a1-cad0f566d31b)

## Excluded links by reason

- auto-linked-filename: 36
  - implementation-notes.md (39edaecf-ce6b-809e-89cd-e924a720cefe, Prompting)
  - claude.md (340daecf-ce6b-8018-a6e4-ca5a70db8beb, Skills)
  - claude.md (352daecf-ce6b-80a4-8556-c2677ae8514a, Skills)
  - claude.md (352daecf-ce6b-8045-9fe1-d1eaa919a1b2, Skills)
  - claude.md (352daecf-ce6b-8032-bc80-fe1d98b6c6bc, Skills)
  - skill.md (353daecf-ce6b-80ef-9ee9-ff911503d4d1, Skills)
  - skill.md (353daecf-ce6b-807c-9028-ccf82572e64a, Skills)
  - claude.md (353daecf-ce6b-8086-a018-e1f9f09f2a98, Skills)
  - claude.md (353daecf-ce6b-803c-a92b-c29448c8f73c, Skills)
  - claude.md (353daecf-ce6b-8009-9d52-f7e7f69de6a7, Skills)
  - competitor-research-skill.md (353daecf-ce6b-8084-8720-db460a044a95, Skills)
  - skill.md (353daecf-ce6b-8084-8720-db460a044a95, Skills)
  - skill.md (353daecf-ce6b-80e0-b7a8-d0239b60e3c7, Skills)
  - download-ggml-model.sh (353daecf-ce6b-8063-988d-fdb864238b66, Skills)
  - claude.md (353daecf-ce6b-8033-9332-eda8f189401f, Skills)
  - claude.md (353daecf-ce6b-8081-af44-fe82fde9d87f, Skills)
  - scrape-ads-skill.md (353daecf-ce6b-80d1-94d1-e3cfce1da3e9, Skills)
  - skill.md (353daecf-ce6b-80d1-94d1-e3cfce1da3e9, Skills)
  - claude.md (353daecf-ce6b-8076-881b-ef65e98197a7, Skills)
  - skill.md (353daecf-ce6b-800f-afd8-e032d401c15e, Skills)
  - claude.md (353daecf-ce6b-801b-8491-d0a58e7b3fde, Skills)
  - claude.md (353daecf-ce6b-8098-b4eb-e9a06fd79392, Skills)
  - ad-brief-yyyy-mm-dd.md (353daecf-ce6b-8091-bd5f-c12db2971123, Skills)
  - claude.md (353daecf-ce6b-80a0-acd5-fb4eea86a4dd, Skills)
  - ad-brief-skill.md (353daecf-ce6b-80c7-a9d9-ccee4120ee2c, Skills)
  - skill.md (353daecf-ce6b-80c7-a9d9-ccee4120ee2c, Skills)
  - claude.md (32cdaecf-ce6b-800c-89ab-d41d74efae01, Field notes)
  - claude.md (32cdaecf-ce6b-8091-864e-d751c06ab1b3, Field notes)
  - claude.md (32cdaecf-ce6b-801e-b17a-d6c3b41119c8, Field notes)
  - claude.md (32cdaecf-ce6b-807f-ac0b-e8b700a66864, Field notes)
  - claude.md (32cdaecf-ce6b-807c-9e58-e72c2ad79e2a, Field notes)
  - scratchpad.md (32cdaecf-ce6b-80be-9601-fb7d6e925348, Field notes)
  - plan.md (32cdaecf-ce6b-80be-9601-fb7d6e925348, Field notes)
  - claude.md (342daecf-ce6b-80f9-b612-ef32ff2a6d30, Field notes)
  - claude.md (31bdaecf-ce6b-80a1-9b1c-f4294fa11cda, n8n with Claude Code)
  - claude.md (31bdaecf-ce6b-8087-af4b-ea99a723254b, n8n with Claude Code)
- config-exclude_urls: 6
  - https://x.com/RoundtableSpace/status/2076597439189111272 (39edaecf-ce6b-80ee-a365-d82c4045f9fd, Learn)
  - https://github.com/iamzhihuix/happy-claude-skills (a0187d62-1a98-4220-a443-d27c1f45b1ed, Skills)
  - https://github.com/ggerganov/whisper.cpp (353daecf-ce6b-80c8-9e34-f3cecc6c0fdf, Skills)
  - https://www.instagram.com/p/DYdGvacErNf (e141ece0-d812-4a43-91c2-be980692e209, Prompting)
  - https://codexbar.app (349daecf-ce6b-80db-a56d-c2f149efc38c, Tools and memory)
- email-tracking-redirect: 2
  - elinkb7e.mail.aiwithremy.com (355daecf-ce6b-803a-aedc-e25f91ddd717, Field notes)
  - elinkb7e.mail.aiwithremy.com (355daecf-ce6b-80a2-8165-cf3cfff4d2b2, Tools and memory)
- google-docs: 2
  - docs.google.com (32cdaecf-ce6b-80fd-868d-f8e5a84f5f19, Prompting)
  - docs.google.com (326daecf-ce6b-809a-9878-d097d46d9df4, Prompting)
- google-drive: 3
  - drive.google.com (39ddaecf-ce6b-80e1-9d16-d41b888217e6, Skills)
  - drive.google.com (3a9daecf-ce6b-8055-9653-dc70f96cb6cf, Skills)
- notion: 7
  - www.notion.so (332daecf-ce6b-80f9-bfbd-ebba1ed3b5fb, Skills)
  - www.notion.so (356daecf-ce6b-80b0-9b56-eb09c8c37cad, Skills)
  - www.notion.so (356daecf-ce6b-8045-be74-fbe483b29300, Skills)
  - www.notion.so (356daecf-ce6b-802d-8231-c1d0bbf3b9cc, Skills)
  - www.notion.so (356daecf-ce6b-800d-9d0e-d66615f68c2f, Skills)
  - www.notion.so (356daecf-ce6b-8022-a1bc-e4845accb358, Skills)
  - www.notion.so (356daecf-ce6b-8026-b001-e17017818f14, Skills)
- skool: 3
  - www.skool.com (353daecf-ce6b-8071-815f-d5612fb4e563, Skills)
  - www.skool.com (352daecf-ce6b-804a-826a-d2728940cc49, Skills)
  - www.skool.com (353daecf-ce6b-803b-a114-e3d7b235952d, Skills)
- non-github URLs dropped inside links-only-github subtrees (by host): airtable.com x1, apify.com x2, facebook.com x1, www.kieranflanagan.io x1, www.linkedin.com x1
- config exclude_urls hits:
  - https://x.com/RoundtableSpace/status/2076597439189111272 (39edaecf-ce6b-80ee-a365-d82c4045f9fd)
  - https://github.com/iamzhihuix/happy-claude-skills (a0187d62-1a98-4220-a443-d27c1f45b1ed)
  - https://github.com/ggerganov/whisper.cpp (353daecf-ce6b-80c8-9e34-f3cecc6c0fdf)
  - https://github.com/ggerganov/whisper.cpp (353daecf-ce6b-80c8-9e34-f3cecc6c0fdf)
  - https://www.instagram.com/p/DYdGvacErNf (e141ece0-d812-4a43-91c2-be980692e209)
  - https://codexbar.app (349daecf-ce6b-80db-a56d-c2f149efc38c)

## Entries missing a description (Notion text)

- Collections: awesome claude code - https://github.com/hesreallyhim/awesome-claude-code (350daecf-ce6b-80dd-b939-f9254738d99a)
- Collections: claude code best practice - https://github.com/shanraisshan/claude-code-best-practice (350daecf-ce6b-801e-beec-f4853c958e99)
- Collections: jeffallan.github.io/claude-skills - https://jeffallan.github.io/claude-skills/skills-guide (34fdaecf-ce6b-8035-9a69-fecbafd89a9b)
- Field notes / Context: plugin for memory - https://github.com/supermemoryai/claude-supermemory (32cdaecf-ce6b-8056-82a5-e8480b62abea)
- Field notes / Personal assistant: Memory - https://www.reddit.com/r/ClaudeAI/comments/1r66oo0/how_i_structure_claude_code_projects_claudemd (342daecf-ce6b-80d6-8b10-de827d12e74c)
- Learn: YouTube video ACRd0Ikg_KI - https://www.youtube.com/watch?v=ACRd0Ikg_KI (363daecf-ce6b-805d-8fc7-effd1507d619)
- Learn: YouTube video RAZVk5NPNtE - https://www.youtube.com/watch?v=RAZVk5NPNtE (342daecf-ce6b-80b4-b625-f43e9619a0de)
- Learn: YouTube video ZAaxx3qyT8g - https://www.youtube.com/watch?v=ZAaxx3qyT8g (36edaecf-ce6b-801e-9cbd-ddaa6c31d5dc)
- Learn: YouTube video fVUlrpaWNxg - https://www.youtube.com/watch?v=fVUlrpaWNxg (342daecf-ce6b-8034-95dd-efc2f6ed9116)
- Learn: YouTube video mpALXah_PBg - https://www.youtube.com/watch?v=mpALXah_PBg (33bdaecf-ce6b-800c-ad4f-c61afcc9450a)
- Learn: YouTube video wkv2ifxPpF8 - https://www.youtube.com/watch?v=wkv2ifxPpF8 (355daecf-ce6b-80d0-8ef5-ca8eceea0abb)
- Learn: thevibefounder.com/r - https://thevibefounder.com/r/loops (39cdaecf-ce6b-8046-8b8e-d2e2c21143fa)
- Skills / Marketing - Ads & SEO: Marketingskills/Lead Magnets - https://github.com/coreyhaines31/marketingskills/tree/main/skills/lead-magnets (356daecf-ce6b-80c0-a405-fd4eb9c116c1)
- Skills / Token burn & models: Omniroute - https://github.com/diegosouzapw/OmniRoute (3a9daecf-ce6b-80ee-9e83-fa34ee3a3e09)
- Tools and memory: anthropics/claude-code - https://github.com/anthropics/claude-code (394daecf-ce6b-8095-a378-e5dc298f271a)
- Tools and memory: rohitg00/agentmemory - https://github.com/rohitg00/agentmemory (396daecf-ce6b-8037-8252-c0b36b847d3e)
- n8n with Claude Code: czlonkowski/n8n-skills - https://github.com/czlonkowski/n8n-skills (31bdaecf-ce6b-8087-af4b-ea99a723254b)

## Entries named from their URL (no usable link text)

- YouTube video ACRd0Ikg_KI - https://www.youtube.com/watch?v=ACRd0Ikg_KI (363daecf-ce6b-805d-8fc7-effd1507d619)
- YouTube video fVUlrpaWNxg - https://www.youtube.com/watch?v=fVUlrpaWNxg (342daecf-ce6b-8034-95dd-efc2f6ed9116)
- YouTube video mpALXah_PBg - https://www.youtube.com/watch?v=mpALXah_PBg (33bdaecf-ce6b-800c-ad4f-c61afcc9450a)
- YouTube video RAZVk5NPNtE - https://www.youtube.com/watch?v=RAZVk5NPNtE (342daecf-ce6b-80b4-b625-f43e9619a0de)
- YouTube video wkv2ifxPpF8 - https://www.youtube.com/watch?v=wkv2ifxPpF8 (355daecf-ce6b-80d0-8ef5-ca8eceea0abb)
- YouTube video ZAaxx3qyT8g - https://www.youtube.com/watch?v=ZAaxx3qyT8g (36edaecf-ce6b-801e-9cbd-ddaa6c31d5dc)
- theaileverage.beehiiv.com/p - https://theaileverage.beehiiv.com/p/top-5-claude-code-front-end-skills (35fdaecf-ce6b-8076-8bc7-f248b6a47d84)
- jeffallan.github.io/claude-skills - https://jeffallan.github.io/claude-skills/skills-guide (34fdaecf-ce6b-8035-9a69-fecbafd89a9b)
- thevibefounder.com/r - https://thevibefounder.com/r/loops (39cdaecf-ce6b-8046-8b8e-d2e2c21143fa)
- rohitg00/agentmemory - https://github.com/rohitg00/agentmemory (396daecf-ce6b-8037-8252-c0b36b847d3e)
- anthropics/claude-code - https://github.com/anthropics/claude-code (394daecf-ce6b-8095-a378-e5dc298f271a)
- YouTube video O2k_qwZA8HU - https://www.youtube.com/watch?v=O2k_qwZA8HU (33adaecf-ce6b-8013-90f1-e157391faa33)
- steipete/CodexBar (CodexBar-0.22.zip) - https://github.com/steipete/CodexBar/releases/download/v0.22/CodexBar-0.22.zip (349daecf-ce6b-80f3-a0ed-de4aee7469eb)
- apps.apple.com/us - https://apps.apple.com/us/app/usage-for-claude/id6755173244 (349daecf-ce6b-801a-a9b3-defb06a07c2a)

## Promoted entries (github URL rescued from a block whose primary was a duplicate)

- https://github.com/czlonkowski/n8n-skills (block 31bdaecf-ce6b-8087-af4b-ea99a723254b describes czlonkowski/n8n-mcp)

## Description taken from the parent block

- YouTube video O2k_qwZA8HU (33adaecf-ce6b-8013-90f1-e157391faa33)
- steipete/CodexBar (CodexBar-0.22.zip) (349daecf-ce6b-80f3-a0ed-de4aee7469eb)
- apps.apple.com/us (349daecf-ce6b-801a-a9b3-defb06a07c2a)

## Entries renamed by a later block that names them (first mention was URL-only)

- ComposioHQ/awesome-claude-skills (competitive-ads-extractor) -> ComposioHQ/awesome-claude-skills/competitive-ads-extractor (36edaecf-ce6b-80c5-a043-e0669e3d20a4)

## Name collisions (same normalized name, different URL)

- none

## ROTATE warnings (secret-shaped text found on the private side)

- ROTATE: 31bdaecf-ce6b-8044-980e-e686b717519d

## Denylist

- private-side hits (expected, not published): 2
- public-side hits: 0 (any hit aborts the run with exit 3)

## Second source (site)

- https://agentmatik.ai/llms-full.txt: fetched=True parsed=62 matched_by_url=36 matched_by_name=15 new=6
- skipped (no repo URL on the site): agents-skills-autoreview, dont-hack-me, larry (LarryLoop), paid-media-skills (Ryze), prompt-guard
- matched by name (site name -> entry): canvas-design -> Canvas Design, code-reviewer (jeffallan) -> Code Reviewer, competitive-ads-extractor -> ComposioHQ/awesome-claude-skills/competitive-ads-extractor, content-research-writer -> Content Research Writer, emil-design-eng -> emil-design-eng, feature-forge -> Feature Forge, find-skills (ClawHub) -> find-skills, frontend-design -> Frontend design, rag-architect -> RAG Architect, secure-code-guardian -> Secure Code Guardian, skill-creator -> skill-creator, spec-miner -> Spec Miner, the-fool -> The Fool, theme-factory -> Theme Factory, webapp-testing -> Web App Testing (official)

## Open decisions (from tools/lint.py)

Refreshed by every `python3 tools/lint.py` run. Each line needs a human decision: fix it in `data/overrides.json` (name, description, url) or change the source in Notion, then re-sync.

- none, lint passes
