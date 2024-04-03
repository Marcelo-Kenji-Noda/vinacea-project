#%%
import rasterio

src = rasterio.open('/mnt/biofeats/assets/TOPOGRAPHY/23S435SN.tif')
raster_data = src.read(1)  # Read the first band
print(src.shape)

# %%
print(src.bounds)
# %%
print(src.csr)
# %%
