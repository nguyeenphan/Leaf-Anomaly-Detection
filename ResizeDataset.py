import os
import shutil
import random

# Đường dẫn đến dataset gốc và dataset mới
source_dir = '/Users/nguyenphan/Developer/Leaf-Anomaly-Detection/new-plant-diseases-dataset/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)'  # Thay bằng đường dẫn đến dataset gốc
target_dir = '/Users/nguyenphan/Developer/Leaf-Anomaly-Detection/grape-only-dataset'  # Thay bằng đường dẫn đến dataset mới
sample_ratio = 0.2  # Tỷ lệ ảnh giữ lại (40%)

# Các lớp liên quan đến grape
grape_classes = [
    'Grape___Esca_(Black_Measles)',
    'Grape___healthy',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___Black_rot'
]

# Tạo dataset mới chỉ chứa các lớp grape
for split in ['train', 'valid']:
    source_split = os.path.join(source_dir, split)
    target_split = os.path.join(target_dir, split)
    os.makedirs(target_split, exist_ok=True)
    
    for grape_class in grape_classes:
        source_class = os.path.join(source_split, grape_class)
        target_class = os.path.join(target_split, grape_class)
        
        if os.path.exists(source_class):
            # Tạo thư mục cho lớp trong dataset mới
            os.makedirs(target_class, exist_ok=True)
            
            # Lấy danh sách ảnh
            images = os.listdir(source_class)
            # Lấy mẫu ngẫu nhiên theo tỷ lệ
            sample_size = int(len(images) * sample_ratio)
            sampled_images = random.sample(images, sample_size)
            
            # Copy ảnh được chọn sang dataset mới
            for img in sampled_images:
                shutil.copy(
                    os.path.join(source_class, img),
                    os.path.join(target_class, img)
                )

# Kiểm tra số lượng ảnh trong dataset mới
for split in ['train', 'valid']:
    print(f"\nSố lượng ảnh trong {split}:")
    split_dir = os.path.join(target_dir, split)
    for grape_class in os.listdir(split_dir):
        class_path = os.path.join(split_dir, grape_class)
        if os.path.isdir(class_path):
            num_images = len(os.listdir(class_path))
            print(f"{grape_class}: {num_images} ảnh")