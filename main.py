# Mohamad Mehdi
# May 1st, 2023
# it is what it is

import os

# ask user for input and output file names
folder = input("Please enter the folder where the .bam files are located: ")
input_bam_file = input("Please enter the name of the input .bam file: ")
output_bam_file = input("Please enter the name of the output .bam file: ")

# concatenate bam files
concat_command = f"samtools cat {os.path.join(folder, input_bam_file)} > {os.path.join(folder, output_bam_file)}"
os.system(concat_command)
print(f"{input_bam_file} has been concatenated into {output_bam_file}")

# convert to sam format
output_sam_file = os.path.splitext(output_bam_file)[0] + ".sam"
convert_command = f"samtools view -h {os.path.join(folder, output_bam_file)} > {os.path.join(folder, output_sam_file)}"
os.system(convert_command)
print(f"{output_bam_file} has been converted to {output_sam_file}")

# run sam2consensus.py
sam2consensus_command = f"python3 sam2consensus.py -i {os.path.join(folder, output_sam_file)} -o {folder}"
os.system(sam2consensus_command)
print(f"{output_sam_file} has been processed by sam2consensus.py")
