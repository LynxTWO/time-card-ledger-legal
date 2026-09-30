# Time Card Ledger legal pages

This public repository hosts the privacy policy and support information for
**Time Card Ledger**, published by Daniel Boyd.

- Privacy policy: <https://lynxtwo.github.io/time-card-ledger-legal/privacy/>
- Support: <https://lynxtwo.github.io/time-card-ledger-legal/support/>
- Third-party licenses: <https://lynxtwo.github.io/time-card-ledger-legal/licenses/>
- Public support email: <danielboyd.apps@gmail.com>

The repository intentionally contains only public legal/support content. The
application source remains in a separate private repository. The pages contain
no analytics, advertising, cookies, forms, remote fonts, or client-side
JavaScript.

Copyright 2026 Daniel Boyd. All rights reserved.

## Notice page presentation

`licenses/THIRD_PARTY_NOTICES.txt` remains the downloadable inventory. Its bytes
and the page's publication/review statements are not changed by the renderer.
The HTML page presents headings, scrollable package tables and expandable
verbatim license text. It needs no browser JavaScript or external requests.

To refresh after an intentional inventory update, use Python 3 with the existing
`markdown-it-py` build tool (verified with 3.0.0):

```sh
python3 scripts/render_notices.py
python3 scripts/render_notices.py --check
python3 -m unittest discover -s scripts -p 'test_*.py'
```

The checks preserve every fenced license text, local anchors, escaping and
repeatable output. Changing presentation does not complete the publisher's
package/native dependency review. Roll back the HTML/CSS renderer change
without changing the downloadable file. Keep private app source and account
or device information out of this public repository.

## September 2026 site update

The language guide previews the next 17-language update; it does not claim store
availability. Language names have their own HTML language tags, with isolated
right-to-left names. App languages and website translations are separate.

The owner approved the narrow privacy/support corrections on September 30:
scope the existing notice to offline features, identify Connected as online
testing, and distinguish encrypted signed packages from public pairing files and
ordinary exports. This is not the complete Connected release notice. Its data
flows, processors, retention and deletion disclosures still need a separate
release review. The in-app/source-policy materials must be reconciled with that
review before Connected ships.

No accounts, analytics, scripts or services were added to this site. The notice
inventory and license text remain byte-for-byte unchanged. To roll back, revert
the website update commit; no app state or stored data is affected.

Validation for this update: 20 browser cases across five pages, 320px/1280px and
light/dark; keyboard skip links and page overflow checked; 858 local links and
anchors resolved. The existing four notice-renderer tests and generated-output
check pass. The downloadable license inventory is unchanged. These checks cover
web structure, layout and keyboard behavior, not heard screen-reader output.
