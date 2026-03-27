# Glyph Vectorization

## 依賴安裝 (Dependencies)

在執行腳本前，請確保已安裝以下系統軟體與 Python 套件：

### 系統軟體 (System Requirements)

1. **Inkscape**
   Inkscape 是一款可以編輯向量圖片的開源程式，支援各大主流作業系統（MacOS、Windows、Linux）。Inkscape 提供 Command Line 的介面可以使用，因此我們可以安裝 Inkscape 再透過 CLI 來讓他幫我們轉換格式。

   **安裝方式**：可以到 [Inkscape 官網](https://inkscape.org/) 下載程式，並將程式的 `bin` 資料夾設定為環境變數。在 Windows 中預設的路徑為 `C:\Program Files\Inkscape\bin`。

### Python 套件 (Python Packages)

需要安裝以下套件以利程式運行，您可以透過 pip 一次安裝：

```bash
pip install cairosvg Pillow tqdm picosvg
```

* `cairosvg`: 主要的 SVG 轉 PNG 處理工具。
* `Pillow` (PIL): 提供圖片處理功能（如轉灰階、高斯模糊與二值化）。
* `tqdm`: 用於顯示命令列進度條。
* `picosvg`: 用於簡化並優化最終輸出的 SVG 路徑。

## 操作步驟 (Execution Steps)

請依序執行以下腳本：

1. **生圖 (SVG to PNG)**:
   ```bash
   python svg2png.py
   ```

2. **轉換路徑 (PNG to SVG)**:
   ```bash
   python potrace.py
   ```

3. **處理 Pico**:
   ```bash
   python run_pico.py
   ```

4. **合併成 SVG Font**:
   ```bash
   python merge_to_svgfont.py
   ```