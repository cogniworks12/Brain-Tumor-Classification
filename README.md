# Brain Tumor Classification

## **Project Overview**
This project is a **deep learning-based brain tumor classification system** that utilizes **Convolutional Neural Networks (CNNs)** to detect and classify brain tumors from MRI images. The model is built using a **sequential CNN architecture**, incorporating techniques such as **dropout regularization, data augmentation, and confusion matrix evaluation** to enhance performance and interpretability.

## **Features**
 Sequential CNN model with dropout for improved generalization  
 Classification of different brain tumor types  
 Data augmentation for enhanced model robustness  
 Confusion matrix analysis for performance evaluation  
 Flask-based web application for real-time predictions  
 GPU-accelerated training for performance optimization  

## **Installation**
To set up the project, follow these steps:

### **1. Clone the Repository**
```bash
git clone https://github.com/cogniworks12/Brain-Tumor-Classification.git
cd Brain-Tumor-Classification
```

### **2. Create and Activate a Virtual Environment**
```bash
python3 -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate  # For Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Application**
```bash
python app.py
```


## **Dataset**
The model is trained using a publicly available **MRI Brain Tumor Dataset** that consists of labeled MRI scans of different tumor types. The dataset undergoes preprocessing techniques such as **data augmentation** to improve generalization and avoid overfitting.

## **Model Training**
The classification model is built using **TensorFlow and Keras**, employing a **sequential CNN architecture** with the following enhancements:
- **Dropout Regularization**: Helps prevent overfitting by randomly deactivating neurons during training.
- **Data Augmentation**: Includes flipping, rotation, and zooming to increase dataset diversity.
- **Confusion Matrix Analysis**: Evaluates model performance by analyzing false positives and false negatives.
- **Training Metrics**: Accuracy, loss, precision, and recall scores for comprehensive evaluation.

## **Usage**
1. Upload an MRI scan image through the web interface.
2. The model processes the image and predicts whether a tumor is present.
3. The classification results are displayed with confidence scores and performance metrics.

## **Contributing**
Pull requests are welcome! If you encounter issues or have suggestions for improvements, feel free to contribute.

## **License**
This project is licensed under the **MIT License**.

---
**Author:** Cogniworks.ai  
🔗 [GitHub](https://github.com/cogniworks12)  
🚀 Powered by AI & Deep Learning

