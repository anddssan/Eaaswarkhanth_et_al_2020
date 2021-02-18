# Install the required packages if needed
install.packages("openxlsx")
install.packages("venn")

# Set working directory to the folder where the header modified Table S1
# is located. If needed, Table S1 should be modified according to image:
# Modify_Table_S1_Header.jpg
setwd("Path:/To/Folder")

library("openxlsx")
library("venn")

df <- read.xlsx("Header_Modified_Table_S1.xlsx", sheet = 1, startRow = 3)

venn(list(df$SNP[df$iHS>=2], df$SNP[df$`XP-EHH.KWT.vs.CEU`>0], 
          df$SNP[df$`XP-EHH.KWT.vs.YRI`>0], df$SNP[df$`XP-EHH.KWT.vs.CHB`>0], 
          df$SNP[df$PBS.KWT.vs.CEU>0], df$SNP[df$PBS.KWT.vs.YRI>0], 
          df$SNP[df$LLRS>0]), 
     zcolor = c("red", "orange", "yellow", "green", "cyan", "blue", "violet"), 
     col = c("red", "orange", "yellow", "green", "cyan", "blue", "violet"))

# The image was further modified using Photoshop (in order to highlight 
# only the value in the intersection of all the sets, and for proper set 
# labelling)