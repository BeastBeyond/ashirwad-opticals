# 👓 Ashirwad Optics - Premium Eyewear & Vision Care

> **Lenskart-Inspired Modern Eyewear & Computerized Eye Testing Portal**  
> Location: *2, Sarjapur - Marathahalli Rd, Near Aggarwal Bhawan, Dommasandra, Chambenahalli, Karnataka 562125*

---

## 🌟 Overview & Key Features

- **👓 Lenskart-Style Top Sticky Navigation**: Grouped categories (*Eyeglasses, Sunglasses, Screen Glasses, Kids & Youth, Contact Lenses, Featured Lineup, 100% Authentic Brands, Computerized Testing, Find Your Vibe, Store Visit*) with smooth scroll redirection.
- **🔍 Frame Shape Roundels Bar**: 7 interactive shape roundels (*Rectangle, Cateye, Aviator, Geometric, Round, Clubmaster, Square*) with deep spotlight modals.
- **✨ 8K Curated Flagship Lineup**: High-resolution 3D perspective tilt cards (*Crystal Clear, Masaba, Bold Signature, The Devil Wears Prada, 2 in 1: Eye + Sun, Feather-light*).
- **🏢 Real In-Store Photo Showcase**: Real store photos featuring the optical display wall, computerized testing room, and frame trays.
- **🔬 State-of-the-Art Computerized Eye Testing**: Detailed 5-step clinical eye examination breakdown.
- **🎯 "Find Your Look" Vibe Matcher**: Multi-persona style filter (*Executive, Minimalist, Bold, Active, Creative*).
- **📍 Store Location & Contact Center**: Live store hours status, embedded Google Maps (`12.879043° N, 77.762585° E`), one-click WhatsApp inquiry, and direct phone call links.
- **Zero Dependencies**: Pure HTML5, CSS3, and Vanilla JavaScript with fast loading and zero build step required.

---

## 💻 How to Open in Visual Studio / VS Code

### Option 1: Open Directly via Terminal
```bash
# Navigate to the project directory
cd /Users/amankumar/.gemini/antigravity-ide/scratch/ashirwad-optics

# Open directly in VS Code
code .
```

### Option 2: Open via Visual Studio Code UI
1. Open **Visual Studio Code**.
2. Click **File** > **Open Folder...** (or `Cmd + O` on macOS).
3. Navigate to `/Users/amankumar/.gemini/antigravity-ide/scratch/ashirwad-optics` and click **Open**.
4. (Optional) Install the **Live Server** extension by Ritwick Dey and click **"Go Live"** at the bottom right to run locally with auto-reload.

---

## 🚀 How to Host this Website on GitHub Pages (Step-by-Step)

### Step 1: Create a New Repository on GitHub
1. Go to [github.com/new](https://github.com/new).
2. Name your repository (e.g., `ashirwad-optics`).
3. Make it **Public** (required for free GitHub Pages).
4. Do **not** initialize with README or .gitignore (we already have them configured).
5. Click **Create repository**.

### Step 2: Push the Code to GitHub
Run the following commands in your terminal from the project folder:

```bash
cd /Users/amankumar/.gemini/antigravity-ide/scratch/ashirwad-optics

# 1. Initialize git and commit all files
git init
git add .
git commit -m "Initial commit: Ashirwad Optics website with high-res assets"

# 2. Rename branch to main
git branch -M main

# 3. Connect your GitHub remote (replace with your actual GitHub username)
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/ashirwad-optics.git

# 4. Push to GitHub
git push -u origin main
```

### Step 3: Enable GitHub Pages (Instant 1-Click Hosting)
1. In your GitHub repository, click on the **Settings** tab.
2. In the left sidebar, click **Pages** (under the "Code and automation" section).
3. Under **Build and deployment** > **Source**:
   - Select **GitHub Actions** (recommended — our included `.github/workflows/deploy.yml` will automatically build and publish).
   - *Or* select **Deploy from a branch** > branch: `main` > folder: `/ (root)` > Click **Save**.
4. Within 1–2 minutes, your website will be live at:
   ```
   https://YOUR_GITHUB_USERNAME.github.io/ashirwad-optics/
   ```

---

## 📂 Project Structure

```
ashirwad-optics/
├── .github/
│   └── workflows/
│       └── deploy.yml          # Automated GitHub Pages deployment
├── assets/                     # 8K studio photography, store images & vector SVGs
│   ├── card_bold_signature.jpg
│   ├── card_crystal_clear.jpg
│   ├── card_devil_wears_prada.jpg
│   ├── card_feather_light.jpg
│   ├── card_masaba.jpg
│   ├── card_two_in_one.jpg
│   ├── contact_lenses_showcase.jpg
│   ├── hero_store_interior.jpg
│   ├── prod_eyeglasses_matte.jpg
│   ├── prod_sunglasses_aviator.jpg
│   ├── store_eye_testing_room.jpg
│   ├── store_frame_tray.jpg
│   ├── store_original_wall.jpg
│   ├── store_titan_tray.jpg
│   └── shape_*.svg             # Infinite-resolution vector frame shapes
├── css/
│   └── styles.css              # Lenskart-inspired design system & sticky navigation
├── js/
│   └── app.js                  # Smooth scrollspy, modals, 3D tilt, vibe filter, live status
├── .gitignore
├── index.html                  # Main semantic HTML structure
└── README.md                   # Project documentation
```

---

## 📞 Store Contact Information

- **Business Name**: Ashirwad Optics
- **Address**: 2, Sarjapur - Marathahalli Rd, Near Aggarwal Bhawan, Dommasandra, Chambenahalli, Karnataka 562125
- **Coordinates**: `12.879043° N, 77.762585° E`
- **Store Hours**: Monday – Sunday: 10:00 AM – 9:30 PM (Open 7 Days)
- **Phone / WhatsApp**: +91 98765 43210
