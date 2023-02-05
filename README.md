# polar-tcx-fix
Fix TCX files from Polar M400 to accept upload to Garmin Connect

## Motivation

Uploading TCX files created with my POLAR M400 to Garmin Connect failed with message "Beim Hochladen der Datei ist ein Fehler aufgetreten. Versuchen Sie es erneut".

The reason are two missing Tags in the `<Author>` section at the end of the file.

In:

```xml
<TrainingCenterDatabase>
  <Author xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Application_t">
    <Name>Polar Flow Mobile Viewer Android</Name>
    <Build>
      <Version>
        <VersionMajor>0</VersionMajor>
        <VersionMinor>0</VersionMinor>
      </Version>
    </Build>
    <LangID>EN</LangID>
    <PartNumber>XXX-XXXXX-XX</PartNumber>
  </Author>
</TrainingCenterDatabase>
```

Out:
```xml
<TrainingCenterDatabase>
  <Author xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Application_t">
    <Name>Polar Flow Mobile Viewer Android</Name>
    <Build>
      <Version>
        <VersionMajor>0</VersionMajor>
        <VersionMinor>0</VersionMinor>
        <BuildMajor>0</BuildMajor>
        <BuildMinor>0</BuildMinor>
      </Version>
    </Build>
    <LangID>EN</LangID>
    <PartNumber>XXX-XXXXX-XX</PartNumber>
  </Author>
</TrainingCenterDatabase>
```

Works for formatted (line breaks) and unformatted (one line) files on my Linux system.


There are other solutions, that fix the TCX by removing the `<Author>` and `<Creator>`, for instance https://hns.se/dev/fapi/fapi.php.

## Script

The script is simple as can be and it works for me. But maybe it can be an template for your issue. Enjoy!