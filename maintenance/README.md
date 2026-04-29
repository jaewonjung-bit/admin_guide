# Enterprise Settings Guide Maintenance

This folder keeps the update process for `chatgpt-codex-enterprise-settings.html` explicit and repeatable.

## Files

- `sources.yml` is the source registry. It defines the official documents that should be checked, the sections they affect, and how often they matter.
- `weekly-refresh-prompt.md` is the shared instruction block for scheduled refreshes and manual Codex requests.

## Weekly operating model

1. Review every `weekly` source in `sources.yml`, then review `monthly` sources when their month is due.
2. Compare the current official source against what the Korean guide currently says. Korean must be checked for both factual freshness and whether any newly documented detail is missing.
3. During the scheduled run, do **not** edit the guide and do **not** commit.
4. Produce a short review report that states:
   - whether there are material source-backed changes,
   - which official sources changed,
   - which guide sections would need updates,
   - and the recommended edits.
5. Send that report as a Codex notification for approval.
6. If multiple official sources disagree, prefer the most recently updated canonical official source, record the conflict in the review report, and avoid silently mixing versions.
7. Only after Jaewon explicitly approves the change should Codex update the Korean body first. Korean is the canonical source of truth for content, depth, and layout.
8. During the Korean update, review terminology for common systems/engineering usage rather than literal translation alone. Keep official product and UI labels in English where that is the more standard operator-facing choice.
9. After updating Korean, Codex must mirror the English version so it is not a summary or shortened adaptation, but the same page in English:
   - same section order and heading hierarchy,
   - same content depth and explanatory coverage,
   - same tables, figures, callouts, examples, code blocks, links, and checklist rows,
   - same visual grouping and layout structure.
10. Any material addition, deletion, or reordering in Korean must be reflected in English in the same update.
11. After mirroring English from Korean, review the English copy against current official English docs so terminology matches the product surface and the latest source wording, not just the Korean source structure.
12. Keep official UI labels and product names in English where that is clearer or matches the product surface.
13. Re-check internal anchors, external source links, image URLs, and KO/EN parity before committing. Structural parity checks are necessary but not sufficient: Codex must also review the English copy against Korean section-by-section to confirm the same semantic coverage and level of detail.
14. If no source-backed change is needed, leave the page untouched and report that briefly.

## Manual Codex update request

When you want a manual refresh, use a request like:

```text
이 레포의 maintenance/sources.yml 기준으로 공식 출처를 다시 확인해서
chatgpt-codex-enterprise-settings.html을 업데이트해줘.
한국어를 기준본으로 유지하고, 영어판은 요약본이 아니라 한국어와 콘텐츠 깊이·구성·레이아웃까지 완전히 동일하게 맞춰줘.
한국어는 일반적인 시스템/기술 용어에 맞게 다시 점검하고, 영어는 최신 공식 영문 문서 표현과 다시 대조해줘.
변경이 없으면 왜 없는지만 짧게 알려줘.
```

That request is the approval step after the weekly review. The weekly automation only checks and reports; manual Codex requests are what apply the approved changes.

## Definition of done

- The guide still cites only source-backed claims.
- Korean remains the canonical source of truth and is checked against the newest official sources before every approved update.
- Korean terminology follows common systems/engineering usage rather than literal translation where a standard Korean technical term exists.
- English remains identical to Korean in section order, heading hierarchy, content depth, examples, tables, figures, links, code blocks, callouts, checklist rows, and visual structure.
- English is also reviewed against the latest official English docs after mirroring so it stays aligned with official product terminology.
- Any Korean-side material change is mirrored in English in the same approved update; English is never allowed to become a shorter summary version.
- The source list at the bottom of the page stays current.
- Broken links, broken figures, and stale screenshot references are removed or replaced.
- Scheduled review jobs never edit or commit.
- Approved manual update jobs commit the final change with a concise maintenance-oriented message.
