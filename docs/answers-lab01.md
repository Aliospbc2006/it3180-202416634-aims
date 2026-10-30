# Trả lời câu hỏi thảo luận – Lab 01

Sinh viên: MSSV 202416634

## Câu hỏi nhanh: cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?

- `git config --global` ghi vào tệp `~/.gitconfig` (trên Windows là `C:\Users\<tên>\.gitconfig`) và áp dụng cho **mọi repo** của người dùng hiện tại trên máy.
- `git config --local` (mặc định khi không có cờ) ghi vào `.git/config` của **riêng repo đó**, không đi theo khi clone và không ảnh hưởng repo khác.
- Khi cùng một khóa xuất hiện ở nhiều mức, mức hẹp hơn thắng: `local` > `global` > `system`. Có thể xem nguồn của từng giá trị bằng `git config --list --show-origin`.
- Trong bài này, các giá trị riêng cho repo (`core.autocrlf`, `pull.rebase`) được đặt ở mức `local` để không làm thay đổi cấu hình chung của máy.

## 1. Vì sao dùng `git mv`?

`git mv a b` tương đương `mv a b` + `git add` cho cả hai đường dẫn, nên thay đổi vào staging ngay dưới dạng một **phép đổi tên**. Git không lưu "đổi tên" như một loại thay đổi riêng mà phát hiện nó bằng độ giống nhau của nội dung (ở đây là 100%). Nhờ vậy:

- Tab *Files changed* của PR hiển thị `renamed` thay vì "xóa tệp cũ + thêm tệp mới".
- `git log --follow -- aims/cart.py` lần theo được lịch sử của tệp qua lần đổi tên, nên không mất truy vết (một yêu cầu của Identification trong SCM).
- Tách commit di chuyển khỏi commit sửa nội dung giúp độ giống nhau giữ ở mức cao, Git nhận ra đổi tên dễ hơn.

## 2. `release/lab01` có phải baseline không?

Có, về mặt khái niệm. Baseline là phiên bản cấu hình đã được thống nhất, đã qua quy trình kiểm soát thay đổi (ở đây là PR #1 đã merge) và được "đóng băng" để làm điểm tham chiếu. `release/lab01` được tạo từ `master` sau khi PR merge, nên nó trỏ đúng vào trạng thái đã duyệt và là bản nộp. Kiểm chứng: `git rev-parse origin/master origin/release/lab01` cho hai mã băm giống nhau.

Lưu ý: nhánh vẫn có thể di chuyển nếu có commit mới, nên để định danh chính xác và bất biến thì cần thêm **tag** (làm ở Lab 04: `v0.1.0` trỏ vào `release/lab01`).

## 3. Vì sao không commit thẳng vào `master` dù làm một mình?

- **Kiểm soát thay đổi:** mọi thay đổi đi qua nhánh + PR để có chỗ mô tả mục đích, xem lại diff và kiểm thử trước khi tích hợp. Tự review vẫn giúp phát hiện lỗi (ví dụ quên sửa `import` sau khi di chuyển tệp).
- **`master` luôn ổn định:** `master` là nguồn để tạo `release/*`; nếu commit dở dang lên đó thì baseline có nguy cơ hỏng.
- **Truy vết và hoàn tác:** mỗi PR là một đơn vị thay đổi có tên, có lịch sử thảo luận, dễ `revert` nguyên cả đơn vị.
- **Tạo thói quen đúng:** quy trình giống khi làm nhóm, và có thể bật *branch protection* để chặn push trực tiếp (Lab 02).
