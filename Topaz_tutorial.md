1. Download [Topaz Photo AI for Windows](https://topazlabs.com/d/photo/latest/win/full)
2. Create a new folder and place **ONLY ONE** MSI file in it. There's no need to make any changes to the filename of MSI file on purpose.
3. Then run the below code in the folder. 

- with **PowerShell**

```powershell
Get-ChildItem -Filter *.msi | ForEach-Object { Start-Process msiexec -ArgumentList "/i `"$($_.FullName)`" /l*v logfile.txt" -Wait }
```

   - or with **Command Prompt (CMD)**

```cmd
for %i in (*.msi) do @msiexec /i "%i" /l*v logfile.txt
```

4. **Directly terminate the installation process when the model file download initiates.**

5. Find required models by keyword search in logfile.txt.

```
Iterating over model files
```

```
not match
```

```
not exist
```

6. Prepend the provided base URL to a model name. 

```
http://models-bal.topazlabs.com/v1/
```

For example, if the model name is `sdi_unet-v2-fp16-64x64-ort.tz2`, then the download link generates as:

```
http://models-bal.topazlabs.com/v1/sdi_unet-v2-fp16-64x64-ort.tz2
```

7. [Extract URLs in text](https://www.convertcsv.com/url-extractor.htm)
8. Use [IDM](https://www.internetdownloadmanager.com/download.html) for faster downloads; enable a proxy and activate global mode if speed is slow or failed downloads.
