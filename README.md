# Laptop Price Predictor

A machine learning web application that predicts laptop prices based on various specifications using a RandomForest Regressor model.

## 🚀 Features

- **Interactive Web Interface**: Built with Streamlit for easy-to-use predictions
- **High Accuracy**: Model achieves 99.9% training accuracy and 99.95% test accuracy
- **Comprehensive Inputs**: Takes into account all major laptop specifications:
  - Brand selection
  - Processor Speed (GHz)
  - RAM Size (GB)
  - Storage Capacity (GB)
  - Screen Size (inches)
  - Weight (kg)

## 📊 Model Performance

- **Training Score**: 99.99%
- **Test Score**: 99.95%
- **Algorithm**: RandomForest Regressor
- **Dataset**: 1000+ laptop records

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.7+
- Required packages: streamlit, pandas, numpy, scikit-learn, joblib

### Setup
1. Clone the repository:
```bash
git clone https://github.com/Bhavya1481/Laptop_price-predictor.git
cd Laptop_price-predictor
```

2. Install dependencies:
```bash
pip install streamlit pandas numpy scikit-learn joblib
```

3. Train the model (optional - model file included):
```bash
python train_model.py
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```

5. Open your browser and go to `http://localhost:8501`

## 📁 Project Structure

```
Laptop_price-predictor/
├── app.py                 # Streamlit web application
├── train_model.py         # Model training script
├── Laptop_price.csv       # Dataset
├── Untitled.ipynb        # Jupyter notebook with analysis
├── rf_model.pkl          # Trained model (generated)
└── README.md             # This file
```

## 🎯 How to Use

1. Open the web application in your browser
2. Fill in the laptop specifications:
   - Select brand from dropdown
   - Enter processor speed in GHz
   - Specify RAM size in GB
   - Set storage capacity in GB
   - Input screen size in inches
   - Enter weight in kg
3. Click "Price Estimation Button!"
4. View the predicted laptop price

## 📈 Dataset

The model is trained on a dataset containing laptop specifications and their corresponding prices, including:
- Brand information
- Technical specifications (processor, RAM, storage)
- Physical attributes (screen size, weight)
- Price data for supervised learning

## 🔧 Model Details

- **Algorithm**: RandomForest Regressor
- **Features**: 6 input features (Brand, Processor_Speed, RAM_Size, Storage_Capacity, Screen_Size, Weight)
- **Training**: 80% of data used for training, 20% for testing
- **Random State**: Fixed for reproducible results

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📧 Contact

For questions or suggestions, please contact [bhavyachaudhari2003@gmail.com](mailto:bhavyachaudhari2003@gmail.com)
