# Enterprise Settings Guide Maintenance

This folder keeps the update process for `chatgpt-codex-enterprise-settings.html` explicit and repeatable.

## Files

- `sources.yml` is the source registry. It defines the official documents that should be checked, the sections they affect, and how often they matter.
- `weekly-refresh-prompt.md` is the shared instruction block for scheduled refreshes and manual Codex requests.

## Weekly operating model

1. Review every `weekly` source in `sources.yml`, then review `monthly` sources when their month is due.
2. Compare the current official source against what the guide currently says.
3. During the scheduled run, do **not** edit the guide and do **not** commit.
4. Produce a short review report that states:
   - whether there are material source-backed changes,
   - which official sources changed,
   - which guide sections would need updates,
   - and the recommended edits.
5. Send that report as a Codex notification for approval.
6. Only after Jaewon explicitly approves the change should Codex update the Korean body first, then mirror the English version so the section order, heading depth, tables, figures, and internal links stay structurally identical to Korean.
7. Keep official UI labels and product names in English where that is clearer or matches the product surface.
8. Re-check internal anchors, external source links, image URLs, and KO/EN structural parity before committing.
9. If no source-backed change is needed, leave the page untouched and report that briefly.

## Manual Codex update request

When you want a manual refresh, use a request like:

```text
이 레포의 maintenance/sources.yml 기준으로 공식 출처를 다시 확인해서
chatgpt-codex-enterprise-settings.html을 업데이트해줘.
한국어를 기준본으로 유지하고 영어판은 구조가 완전히 동일하게 맞춰줘.
변경이 없으면 왜 없는지만 짧게 알려줘.
```

That request is the approval step after the weekly review. The weekly automation only checks and reports; manual Codex requests are what apply the approved changes.

## Definition of done

- The guide still cites only source-backed claims.
- Korean remains the baseline language.
- English remains structurally identical to Korean.
- The source list at the bottom of the page stays current.
- Broken links, broken figures, and stale screenshot references are removed or replaced.
- Scheduled review jobs never edit or commit.
- Approved manual update jobs commit the final change with a concise maintenance-oriented message.
