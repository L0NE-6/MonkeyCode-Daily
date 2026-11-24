# Third-Party Notices

This repository is distributed under the MIT License in [LICENSE](LICENSE).

## MonkeyCode protocol implementation

The check-in flow, Cap challenge algorithm, endpoint names, and request/response
field names were implemented against the fixed source revision below:

- Project: `ProvidersPlugin/Agent2Providers`
- Revision: `b35b163d01fc3effb30ae40a012fd657fdc0a54d`
- Relevant files:
  - `wasm/sdk/src/monkeycode_checkin.rs`
  - `wasm/monkeycode/src/endpoints.rs`
  - `wasm/monkeycode/src/lib.rs`
  - `wasm/monkeycode-intl/src/endpoints.rs`
- Host reference for the Cap calculation:
  - `Agent2API-Deploy/desktop-tauri/src-tauri/server/src/server/core/plugin_host/wasm/monkeycode_cap.rs`

The referenced project is licensed under AGPL-3.0-only. Its source is available
from its public repository. No upstream source file is copied verbatim into this
repository; the protocol behavior is reimplemented in Python for this project.

## Python dependency

`requests` is used under the Apache License 2.0. See the installed package's
license metadata and `requests` distribution for the full text.

## Trademarks

MonkeyCode, related service names, and logos are trademarks or service marks of
their respective owners. This project is an independent client and is not
affiliated with or endorsed by MonkeyCode.
