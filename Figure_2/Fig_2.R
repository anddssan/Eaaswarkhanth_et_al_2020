# Install the required package if needed.
install.packages("chromoMap")

# Set working directory to the folder where the .txt files are located.
setwd("Path:/To/Folder")

# Load the required package.
library("chromoMap")

# Create the chromosomal map.
chromoMap("chromosome_file.txt","annotation_file.txt",
          # Chromosome file provided. The annotation file is a 
          # tab-delimited .txt file created using the values from 
          # Table S3 minus the header.
          data_based_color_map = T,
          data_type = "numeric",
          aggregate_func = "sum",
          legend = T,
          data_colors = list(c("blue","red")),
          chr_color = c("gray"),
          chr_width = 15, 
          lg_x = 50,
          lg_y = 250)

# The output was further modified using an image editor (in order to 
# enhance overall readability).
