import argparse
import zipfile as zf

parser = argparse.ArgumentParser(
    description="Create a ZIP archive containing a highly compressible file."
)

parser.add_argument(
    "-s", "--size",
    type=float,
    required=True,
    help="Size Of Uncompressed File In GB."
)

parser.add_argument(
    "-nz", "--zip-name",
    default="zip.zip",
    help="Output Zipfile Name.(Optional, default=zip.zip)"
)

parser.add_argument(
    "-nf", "--file-name",
    default="data.txt",
    help="Name of the data file txt.(optional, default=data.txt)"
)

args = parser.parse_args()

size_in_bytes = int(args.size * 1_000_000_000)
chunk_size = 1024 * 1024
chunk = b"0" * chunk_size

with zf.ZipFile(args.zip_name, "w", compression=zf.ZIP_DEFLATED) as Z:
    with Z.open(args.file_name, "w") as F:
        remaining = size_in_bytes
        while remaining > 0:
            n = min(chunk_size, remaining)
            F.write(chunk[:n])
            remaining -= n

print(f"Created {args.zip_name}")