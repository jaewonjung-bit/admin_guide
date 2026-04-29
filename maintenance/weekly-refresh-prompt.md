# Weekly Refresh Prompt

Review the official sources listed in `maintenance/sources.yml` against `chatgpt-codex-enterprise-settings.html`.

Use Korean as the baseline version of the guide when assessing impact.

During the scheduled weekly run:

1. Do not edit files.
2. Do not commit changes.
3. Produce a concise review report that says whether there are material source-backed changes, which official sources changed, which guide sections would need updates, and what the recommended edits are.
4. If there is no material source-backed change, say that briefly.
5. Open a Codex notification/inbox item with the review result for approval.

Before finishing, verify:

1. All relevant weekly sources in `maintenance/sources.yml` were checked.
2. Any due monthly sources were checked.
3. The report clearly distinguishes "needs update" from "no material change".

After explicit user approval in a later manual run, update the Korean guide first, then update the English version so the section order, heading depth, tables, figures, internal anchors, and overall information architecture remain structurally identical to Korean. At that time, keep the guide source-backed, preserve official product and UI labels where appropriate, replace stale links or obsolete image references, verify KO/EN structural parity plus internal anchors and outbound links, and commit the approved change.
