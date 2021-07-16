library(devtools)
install_version('wmtsa', version='2.0.3', repos = "http://cran.us.r-project.org")
library(wmtsa)
library(doParallel)
cl=makeCluster(6)
registerDoParallel(cl)


#########################Data Import and Preparation####################
setwd('<data_location>')
spectra=read.csv('<file_name>')

#continuous wavelet processing in parallel
#wavelet scales 2, 3, and 4 summed
spectra_cwt=foreach(i=1:nrow(spectra), .combine=rbind) %dopar%
  {
    library(wmtsa)
    temp1=as.numeric(spectra[i,])
    temp1=wavCWT(temp1, n.scale=8, wavelet="Gaussian2")
    temp1[,2]+temp1[,3]+temp1[,4]
  }

#wavelet processing without parallel processing
#wavelet scales 2, 3, and 4 summed
process_cwt=function(x) {
  temp1=wavCWT(as.numeric(x), n.scale=8, wavelet="Gaussian2")
  temp1[,2]+temp1[,3]+temp1[,4]
}

#apply wavelet transform to each row
spectra_cwt=t(apply(spectra, 1, FUN = process_cwt))




