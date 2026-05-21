import os

src_path = r"C:\Users\10pri\.gemini\antigravity\brain\946349d6-6e4d-4a97-bb17-5b12022ad9c8\.system_generated\steps\36\content.md"
dest_path = r"c:\Users\10pri\Downloads\jjp\clone\index.html"

if not os.path.exists(src_path):
    # Fallback to step 3 if step 36 is not found
    src_path = r"C:\Users\10pri\.gemini\antigravity\brain\946349d6-6e4d-4a97-bb17-5b12022ad9c8\.system_generated\steps\3\content.md"

print(f"Reading from: {src_path}")
with open(src_path, "r", encoding="utf-8") as f:
    content = f.read()

parts = content.split("---", 1)
if len(parts) < 2:
    print("Error: Could not find '---' separator in content.")
    exit(1)

html_content = parts[1].strip()

# Ensure target directory exists
os.makedirs(os.path.dirname(dest_path), exist_ok=True)

with open(dest_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully extracted HTML to: {dest_path}")
print(f"Extracted size: {len(html_content)} bytes")
print("First 200 characters of HTML:")
print(html_content[:200])
