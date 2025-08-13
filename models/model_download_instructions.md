# 📥 Model Download Instructions

This project requires the pre-trained **DenseNet-121** model files, which are too large to store directly in the repository.  
They are provided in the [GitHub Releases](https://github.com/HeleenaRobert/opencv-dnn-image-classifier/releases) section.

## Required Files

- `DenseNet_121.caffemodel` – Pre-trained model weights
- `DenseNet_121.prototxt` – Network architecture definition

### How to Set Up

1. Go to the **[Latest Release](https://github.com/HeleenaRobert/opencv-dnn-image-classifier/releases/latest)**.
2. Download both files from the **Assets** section.
3. Place them inside the `models/` folder (a placeholder folder is already included in this repo).
4. Ensure the file paths in the code point to `models/DenseNet_121.caffemodel` and `models/DenseNet_121.prototxt`.

> ⚠ Without these files, the classifier will not run, as they contain the trained network weights and architecture.

---

### 📚 Original Source

These model files were originally obtained from the open-source **[DenseNet-Caffe](https://github.com/shicai/DenseNet-Caffe)** repository:  

- Pre-trained weights: `DenseNet_121.caffemodel`  
- Network architecture: `DenseNet_121.prototxt` (deploy file)  

They are redistributed here for convenience under the same open license provided by the original authors.
