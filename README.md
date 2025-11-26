
# AI-fruit-veg-detection

This is a smart AI-based detection system designed to replace the current weighing scale workflow. When a product is placed on the scale, the system automatically detects the product and assigns the correct label. This significantly reduces customer queue time.

It is designed specifically for fruit and vegetable markets. The current accuracy level is approximately 85–100%, and any untrained items are handled as “unknown.”


## Setup and Run Instructions (Raspberry Pi)

1. Clone the repository

```bash
git clone https://github.com/amalaseeli-VBR/AI-fruit-veg-detection.git

```
2. Change directory
```bash
cd AI-fruit-veg-detection
```

3. Create a virtual environment

```bash
python3 -m venv virtualenv
```

4. Activate the environment

```bash
virtualenv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Run the script
```bash
python fruit_detection.py
```
## Authors

- [Amalaseeli](https://github.com/amalaseeli-VBR)

