# University Example App

## Description

An app which accepts raw detector camera feeds from 2 nearby cameras (contained in `data_1.txt` and `data_2.txt`) and
uses it to calculate the average time duration and vehicle speed to pass the distance between the cameras.

## Example Data

Example data (contained in `data_1.txt` and `data_2.txt`) showcases the structure of raw data feed, but doesn't mimic it
entirely and should be updated according to required specifications, along with the code.

## Development

To run the code use the command below:

```
  python app.py
```

In case of errors with reading files, make sure there's no new empty lines at the end and that the path is correct.