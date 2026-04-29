# Enterprise Settings Guide Maintenance

This folder keeps the update process for `chatgpt-codex-enterprise-settings.html` explicit and repeatable.

## Files

- `sources.yml` is the source registry. It defines the official documents that should be checked, the sections they affect, and how often they matter.
- `weekly-refresh-prompt.md` is the shared instruction block for scheduled refreshes and manual Codex requests.

## Weekly operating model

1. Review every `weekly` source in `sources.yml`, then review `monthly` sources when their month is due.
2. Compare the current official source against what the guide currently says.
3. Update the Korean body first. Korean is the baseline version of the page.
4. Update the English version so the section order, heading depth, tables, figures, and internal links stay structurally identical to Korean.
5. Keep official UI labels and product names in English where that is clearer or matches the product surface.
6. Re-check internal anchors, external source links, image URLs, and KO/EN structural parity before committing.
7. If no source-backed change is needed, do not churn the page. Record that the review found no material change.

## Manual Codex update request

When you want a manual refresh, use a request like:

```text
이 레포의 maintenance/sources.yml 기준으로 공식 출처를 다시 확인해서
chatgpt-codex-enterprise-settings.html을 업데이트해줘.
한국어를 기준본으로 유지하고 영어판은 구조가 완전히 동일하게 맞춰줘.
변경이 없으면 왜 없는지만 짧게 알려줘.
```

That request is intentionally the same workflow used by the weekly automation, so scheduled and manual updates stay aligned.

## Definition of done

- The guide still cites only source-backed claims.
- Korean remains the baseline language.
- English remains structurally identical to Korean.
- The source list at the bottom of the page stays current.
- Broken links, broken figures, and stale screenshot references are removed or replaced.
- The final change is committed with a concise maintenance-oriented message.
