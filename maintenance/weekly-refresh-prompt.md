# Weekly Refresh Prompt

Review the official sources listed in `maintenance/sources.yml` against `chatgpt-codex-enterprise-settings.html`.

Use Korean as the canonical source of truth for the guide when assessing impact.

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

After explicit user approval in a later manual run:

1. Update the Korean guide first.
2. Treat Korean as the canonical source of truth for content, depth, and layout.
3. Update the English version so it is the same page in English, not a shortened summary:
   - same section order and heading hierarchy,
   - same content depth and explanatory coverage,
   - same tables, figures, callouts, examples, code blocks, links, and checklist rows,
   - same visual grouping and layout structure.
4. Mirror every material Korean-side addition, deletion, or reordering in English during the same approved update.
5. Keep the guide source-backed, preserve official product and UI labels where appropriate, and replace stale links or obsolete image references.
6. Run `python3 maintenance/verify-bilingual-parity.py`, then perform a section-by-section manual review to confirm that English matches Korean in semantic coverage and level of detail, not just element counts.
7. Verify internal anchors and outbound links, then commit the approved change.
