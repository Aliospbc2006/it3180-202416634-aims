# Trả lời câu hỏi thảo luận – Lab 04

Sinh viên: MSSV 202416634

## 1. Vì sao chuẩn bị phát hành (version, CHANGELOG) trên `master` trước, không sửa trên nhánh `release`?

- Mọi thay đổi vào cấu hình đều phải đi qua PR vào `master` để được review; nhánh `release/*` được bảo vệ và chỉ nhận thay đổi từ PR.
- Nếu sửa số phiên bản/CHANGELOG trực tiếp trên `release/*` thì `master` không có các thay đổi đó; hai dòng lệch nhau và về sau phải đồng bộ ngược, mà quy tắc là `release/*` không merge ngược vào `master`.
- Khi chuẩn bị trên `master`, `release/lab04` được tạo ra đã chứa sẵn đúng nội dung cần phát hành, nên baseline vừa được duyệt vừa "đóng băng" ngay từ đầu.

## 2. Vì sao `release/*` không bao giờ merge ngược vào `master`?

- `release/*` là dòng **bảo trì** của một bản đã giao; nó chỉ nhận bản vá cần thiết. Nó không chứa tính năng mới của `master` nên merge ngược sẽ kéo theo những thay đổi riêng của dòng bảo trì (ví dụ số phiên bản `1.0.1`) và gây xung đột với `master` đã tiến tới `1.1.0`.
- Bản sửa lỗi cần có ở cả hai nơi được lan truyền có chủ đích bằng `cherry-pick -x` (Lab 05): chỉ đúng commit sửa lỗi đi sang, có ghi nguồn gốc.
- Giữ chiều đi một hướng (`master` → `release/*`) làm lịch sử rõ ràng, dễ kiểm toán.

## 3. So sánh với GitFlow

| | Release Flow (học phần) | GitFlow |
|---|---|---|
| Nhánh tích hợp | Chỉ `master` | `develop` + `main` |
| Nhánh release | `release/*` tạo từ `master`, **không merge ngược** | `release/*` tạo từ `develop`, merge vào **cả** `main` và `develop` |
| Hotfix | Tạo từ `release/*`, rồi cherry-pick về `master` | Tạo từ `main`, merge vào `main` và `develop` |
| Độ phức tạp | Ít nhánh dài hạn, gọn | Nhiều nhánh dài hạn, dễ "merge hell" |

## 4. Vì sao lên `1.0.0` mà không phải `0.4.0`?

Theo SemVer, `0.y.z` là giai đoạn đầu, API chưa ổn định (`v0.1.0`–`v0.3.0` ứng với Lab 01–03). `1.0.0` đánh dấu lần đầu có bản phát hành đủ ổn định để giao cho người dùng: có đủ chức năng giỏ hàng, tìm kiếm, giảm giá, có bộ test hồi quy và quy trình phát hành. Từ đây số phiên bản mang ý nghĩa tương thích: sửa lỗi tăng PATCH, thêm tính năng tương thích tăng MINOR, phá vỡ tương thích tăng MAJOR.
