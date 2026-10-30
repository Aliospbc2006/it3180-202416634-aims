# Changelog

Định dạng theo [Keep a Changelog](https://keepachangelog.com/), đánh số phiên bản theo [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.1.0] - 2026-10-30
### Added
- `Cart.sort_by_title()` và `Cart.sort_by_cost()` sắp xếp giỏ hàng.
- `search_by_category()` tìm đĩa theo thể loại.

## [1.0.0] - 2026-10-30
### Added
- `Cart.print_cart()` in chi tiết giỏ hàng; giỏ trống in "The cart is empty".
- `search_by_title()` tìm đĩa theo tiêu đề.
- `Cart.total_cost_with_discount(percent)` tính tổng tiền sau giảm giá, kiểm tra `percent` trong 0–100.
- Thông báo thêm đĩa bằng tiếng Việt.
- Tài liệu: mẫu Pull Request, sơ đồ use case, bộ test `unittest`.

### Changed
- Mã nguồn được gom vào package `aims/`.

### Fixed
- Giỏ hàng nhận đĩa thứ 21 dù giới hạn là 20 (#6).
