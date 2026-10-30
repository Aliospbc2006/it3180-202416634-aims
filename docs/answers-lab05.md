# Trả lời câu hỏi thảo luận – Lab 05

Sinh viên: MSSV 202416634

## 1. Ưu, nhược điểm của *upstream first* so với *release first*

| | Upstream first (sửa ở `master` trước, cherry-pick xuống `release/*`) | Release first (sửa ở `release/*` trước, đưa về `master` sau) |
|---|---|---|
| Ưu | Bản sửa luôn có ở `master`, không bị "quên" ở dòng phát triển; mọi bản sau đều thừa hưởng | Sửa đúng trên mã đang chạy ở bản phát hành, tái hiện lỗi chính xác, ít rủi ro lệch ngữ cảnh |
| Nhược | `master` đã tiến xa, mã có thể khác bản phát hành nên cherry-pick dễ xung đột, phải kiểm thử lại trên release | Dễ quên lan truyền về `master` (hồi quy ở bản sau); phải theo dõi thủ công |
| Phù hợp | Sản phẩm lớn, phát hành theo sprint, `master` là nguồn sự thật | Nộp bài theo tuần, nhiều bản song song (cách học phần dùng) |

Học phần dùng *release first*: tạo `hotfix/*` từ đúng `release/*` bị ảnh hưởng, rồi `cherry-pick -x` sang `master` và các `release/*` khác.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?

- `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"` chỉ thấy **1** bản cherry-pick thay vì 2 (thiếu ở nhánh `release/lab05`).
- `git tag --contains <FIX_SHA>` không liệt kê tag của `release/lab05` (`v1.1.0`).
- `git cherry -v origin/release/lab05 origin/master` hoặc ngược lại hiện dấu `+` cho commit sửa lỗi (nghĩa là nhánh kia chưa có bản tương đương).
- Vòng lặp kiểm tra hành vi: `search_by_title([...], 'lion')` trả về `0` thay vì `1` trên dòng phiên bản thiếu bản sửa.

## 3. Vì sao ở Phần A chưa gắn tag `v1.1.0`?

Tag là định danh **bất biến** của một bản phát hành và không nên xóa hay di chuyển sau khi chia sẻ. Khi tạo `release/lab05`, ta biết trước sẽ còn phải đưa bản vá `search_by_title` vào nhánh này. Nếu đã gắn `v1.1.0` rồi mới sửa, tag sẽ không chứa bản sửa và phải phát hành `v1.1.1`. Chờ bản vá được merge rồi mới gắn tag nên `v1.1.0` đã chứa đầy đủ.

## 4. Vì sao không merge cả nhánh hotfix vào `master`?

Nhánh hotfix có commit nâng phiên bản `1.0.1` (và mục `[1.0.1]` của CHANGELOG) chỉ đúng cho dòng `1.0.x`. Merge nguyên nhánh vào `master` (đã ở `1.1.0`) sẽ xung đột và đặt sai số phiên bản. Vì vậy chỉ `cherry-pick -x` đúng commit sửa lỗi (commit 1); `-x` ghi dòng `(cherry picked from commit <sha>)` để truy vết nguồn gốc.
