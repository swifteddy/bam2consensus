# BAM to Consensus FASTA Converter
This script takes a BAM file, concatenates it, converts it to SAM format, and then uses sam2consensus.py to generate a consensus FASTA file.

## Usage
1. Clone this repository and navigate to the bam2consensus directory.
2. Ensure samtools is installed and in your PATH.
3. Place your BAM file(s) in a directory.
4. Run bam_to_consensus.py.
5. Follow the prompts to enter the input and output file names, don't forget the file extensions. Use the absolute path for the directory.

## Output
* A concatenated BAM file.
* A SAM file generated from the concatenated BAM file.
* A consensus FASTA file generated by sam2consensus.py.

Disclaimer
This script was created for personal use and may not work for all use cases. Use at your own risk. Also still in development.
