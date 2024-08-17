# Ranking-News

## Mô tả dự án

Crawl tin tức từ website [CafeBiz](https://cafebiz.vn/cong-nghe.chn) và xếp hạng các bài viết dựa trên số lượng lượt thích (likes) trên Facebook. 
Dữ liệu sau đó được lưu trữ và sắp xếp để phục vụ cho mục đích phân tích và hiển thị.

## Tính năng chính

- Crawl dữ liệu từ trang web công nghệ của CafeBiz.
- Crawl thông tin về tiêu đề, URL, và số lượng lượt thích trên Facebook của các bài viết.
- Sắp xếp các bài viết theo số lượng lượt thích giảm dần.
- Hiển thị lên server với Flask.

## Cài đặt

### Yêu cầu hệ thống
- Google Chrome
- Thư viện Python: `selenium`, `pandas`, `Flask`

### Hướng dẫn cài đặt

1. **Clone repository từ GitHub:**

   ```bash
   git clone https://github.com/QHanh/Ranking-News.git
   cd Ranking-News