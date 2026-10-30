# Trả lời câu hỏi thảo luận – Lab 02

Sinh viên: MSSV 202416634

## 1. Vì sao phải đồng bộ `master` trước khi gửi PR?

Nhánh của Dev 2 được tạo khi `master` chưa có `print_cart`. Nếu gửi PR ngay, người review chỉ thấy phần thay đổi của nhánh mà không biết nó có hoạt động cùng mã mới nhất hay không. Merge `origin/master` vào nhánh trước giúp:

- Phát hiện và xử lý **xung đột** ngay trên nhánh của mình, không đẩy gánh nặng sang người merge.
- Chạy `python main.py` / test trên **kết quả tích hợp** thực tế; thứ được duyệt chính là thứ sẽ vào `master`.
- Giữ nhánh sống ngắn, gần `master`, tránh "merge hell".

## 2. Khi nào không được rebase?

Không rebase (và không `amend`, `reset`) trên các commit **đã được chia sẻ**: nhánh đã có người khác lấy về, nhánh đã merge, `master`, `release/*`. Rebase viết lại lịch sử, tạo SHA mới; người khác đang dựa trên SHA cũ sẽ bị lệch và phải xử lý lại. Chỉ rebase nhánh riêng chưa ai dùng (và khi push lại phải `--force-with-lease`).

## 3. `feature/*` khác `topic/*` ra sao?

- `feature/<tên>`: thêm **tính năng** của sản phẩm (ví dụ `feature/cart-print`, `feature/search-by-title`); thường có mã nguồn và test, gắn với một yêu cầu.
- `topic/<mô-tả>`: công việc **phụ trợ** không phải tính năng người dùng thấy: tài liệu, cấu hình, mẫu PR, chuẩn bị phát hành (ví dụ `topic/pr-template`, `topic/use-case-diagram`).
- Cả hai đều tạo từ `master`, merge về `master` qua PR; khác nhau chủ yếu ở ngữ nghĩa để nhìn tên nhánh biết mục đích.

## 4. So sánh 3 kiểu merge (thực hiện trong lab)

| | Merge commit (PR #3) | Squash (PR #4) | Rebase (PR #5) |
|---|---|---|---|
| Giữ commit chi tiết | Có | Không (gộp thành 1) | Có (SHA mới) |
| Lịch sử tuyến tính | Không (có commit merge) | Có | Có |
| Revert cả tính năng | 1 lệnh `git revert -m 1` | 1 lệnh | Phải revert nhiều commit |
