**Mục tiêu: Dự đoán/Phân loại 1 người vào 1 trong 3 class: tiểu đường, tiền tiểu đường, không bị bệnh tiểu đường.**            
Biến dự đoán: Diabetes_012.             
*Do dữ liệu mất cân bằng nên ưu tiên dự đoán người có khả năng tiền tiểu đường hoặc tiểu đường và chấp nhận các trường hợp dương tính giả.* **

### Các mục tiêu

1. EDA:      
    Tìm hiểu cấu trúc, phân phối và mối quan hệ giữa các biến.      
    Phát hiện các vấn đề trong dữ liệu. 

2. Làm sạch dữ liệu: Xử lí outliers và mất cân bằng dữ liệu. 
3. Kiểm định các giả thuyết: Xác nhận mối quan hệ giữa các biến. 
4. Xây dựng mô hình cho bài toán phân loại. 
5. Đánh giá mô hình:        
    Đánh giá độ chính xác, độ nhạy, độ đặc hiệu.


### Các phương pháp và chiến lược phân tích 

1. Xử lí outliers       
    Vì các outliers trong bộ data có nghĩa, và logistic regression nhạy cảm với các outliers.       
    Các biến như MentHlth và PhysHlth có rất nhiều giá trị 0 nên không thể dùng log transform.      
    Chiến lược xử lí outliers ở đây là dùng Robust Scaling hoặc chia nhãn lại cho các biến. 

2. Kiểm định các giả thuyết để chọn biến: Chi-square, ANOVA, Kruskal-Wallis. 

3. Xử lí mất cân bằng dữ liệu       
    Nhóm có ít dữ liệu nhất là Pre-Diabetes chiếm ~2% nhưng có khoảng 4000 quan trắc.       
    Có thể dùng cả under-sampling, over-sampling, kết hợp under-over sampling và SMOTE. 

4. Lựa chọn mô hình         
    Bài toán phân loại với K = 3 => dùng Multinomial Logistic.   

    Dùng Naive Bayes nếu thỏa giả định về sự độc lập của các biến.

    Không dùng LDA hay QDA vì yêu cầu tất cả các biến giải thích phải có phân phối chuẩn,       
    trong quá trình EDA cũng phát hiện data có nhiều dữ liệu nhị phân và rời rạc => không thỏa giả định. 

5. Chẩn đoán, Đánh giá mô hình  
    Nếu phát hiện đa cộng tuyến => Sử dụng các phương pháp co hệ số (Regularization)
