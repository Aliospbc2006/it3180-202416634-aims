# Trả lời câu hỏi thảo luận – Lab 03

Sinh viên: MSSV 202416634

## 1. Merge base là gì?

Merge base là **commit tổ tiên chung gần nhất** của hai nhánh (xem bằng `git merge-base A B`). Khi merge, Git thực hiện *ba-way merge* giữa: merge base, đầu nhánh A và đầu nhánh B.

- Dòng chỉ một bên thay đổi so với merge base thì lấy thay đổi của bên đó.
- Dòng **cả hai bên cùng sửa khác nhau** so với merge base thì Git không tự quyết được và báo **xung đột**.

Trong lab, `feature/vietnamese-messages` và `feature/show-added-title` cùng tách từ một commit trên `master` (merge base) và cùng sửa dòng `print(...)` trong `Cart.add_dvd`. Khi PR đầu tiên merge xong, `master` đi tiếp; nhánh thứ hai gặp xung đột vì cùng một dòng đã khác so với merge base ở cả hai phía.

## 2. Vì sao `master` và `release/*` phải dùng `revert`?

- `reset` **viết lại lịch sử** (dời con trỏ nhánh về commit cũ). Trên nhánh đã chia sẻ, người khác đã có các commit bị bỏ; lần `pull` sau sẽ lệch, buộc phải `push --force` và có nguy cơ mất công của người khác.
- `revert` **thêm một commit mới** có nội dung đảo ngược, giữ nguyên lịch sử cũ. An toàn cho nhánh chung, không cần force push, và vẫn truy vết được ai hoàn tác, khi nào, vì sao.
- `master` là nguồn của `release/*` và baseline; `release/*` là bản đã giao. Cả hai cần lịch sử **chỉ tăng** để kiểm toán cấu hình (configuration audit). Vì vậy hoàn tác phải đi qua nhánh + PR như mọi thay đổi khác.
- Khi hoàn tác một **merge commit** phải chỉ rõ nhánh cha cần giữ: `git revert -m 1 <sha>` (cha thứ nhất = `master` trước khi merge). Thiếu `-m` Git báo `commit ... is a merge but no -m option was given`.

## 3. Tóm tắt các việc đã làm

| Phần | Nội dung | PR / Issue |
|---|---|---|
| A | Issue #6, test tái hiện (FAIL) rồi sửa `>` thành `>=`, `Fixes #6` | PR #7 |
| B | Bugfix từ `feature/discount`, PR có base là nhánh tính năng | PR #8, #9 |
| C | Xung đột cùng một dòng, giải quyết bằng merge và thực hành rebase | PR #10, #11 |
| D | `reset --soft/--mixed/--hard`, `reflog`, `revert -m 1` qua PR | PR #12 |
