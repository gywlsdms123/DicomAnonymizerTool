# DicomAnonymizedTool

![image](https://user-images.githubusercontent.com/51704606/151294716-17b868a6-30b5-4ae9-bc78-f8153526b26b.png)
![image](https://user-images.githubusercontent.com/51704606/151297912-bd51bcbd-dff5-44b6-9222-23f4ec6d1ee8.png)

**DicomAnonymizedTool** is an open source software created for those who want to anonymize Dicom files. For those who have a hard time installing the Python environment, I made an .exe  file using python gui. If you specify a folder, this program anonymizes all subdirectories as well. If there are tags you want to add anonymize, you can edit the code.

## Anonymize Tag List 
* Anonymize Tag List
  * PatientName         
  * PatientBirthDate
  * PatientSex
  * OtherPatientIDs
  * PatientAge
  * RequestingPhysician
  * InstitutionName
  * InstitutionAddress
  * ReferringPhysicianName
  * StationName
  * StudyDate
  * SeriesDate
  * AcquisitionDate
  * ContentDate
  * StudyTime
  * SeriesTime
  * AcquisitionTime
  * ContentTime
  * Manufacturer
  * ManufacturerModelName
  * DateOfLastCalibration
  * TimeOfLastCalibration
  * OperatorsName
  * StudyDescription
  * SeriesDescription
  * InstitutionalDepartmentName
  * ProtocolName
  
## Resources

* [Releases](https://github.com/gywlsdms123/DicomAnonymizedTool/releases "DicomAnonymizeTool releases")

## Requirements
- include venv
```
pip install pydicom 
pip install Pyside2
pip install tqdm
```

## Getting Involved
* We use the <a href="../../issues">GitHub issue tracker</a> for all bugs/issues/enhancements

## License
DicomAnonymizedTool is licensed under MIT License.
