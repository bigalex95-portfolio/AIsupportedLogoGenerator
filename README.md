# Image (logo) generation with StyleGANv2

## Usage
### Step 1. Download source codes from github to "Project Folder":
	a)git clone https://github.com/cedricoeldorf/ConditionalStyleGAN
	b)git clone https://github.com/NVlabs/stylegan2
	c)git clone https://github.com/k-l-lambda/stylegan-web
### Step 2. Download and Extract dataset images
### Step 3. Preprocess images: 
	a)crop images to bounding boxes with /"Path to Project Folder"/Code/data_prep.py
	b)scale images with /"Path to Project Folder"/Code/scale.py
### Step 4. Start training as it is written in: 
	/"Path to Project Folder"/Code/ConditionalStyleGAN/readme.md
### Step 5. Start training as it is written in:
	/"Path to Project Folder"/Code/stylegan2/README.md
### Step 6. Copy trained model to:
	/"Path to Project Folder"/stylegan-web/models/
### Step 7. Running web host as it is written in:
	/"Path to Project Folder"/Code/stylegan-web/README.md