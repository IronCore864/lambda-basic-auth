# Lambda Basic Auth

Lambda function doing basic auth.

## Usage

Can be used as lambda edge, together with cloudfront. Using this part for viewer request, then after auth, plant cookie at viewer response. Combining with cloudfront cookie protection, or using WAF to check headers for cookies, so that to protect access.

## Run

Change `usr` and `pwd` from `main.py` to your desired valuesfirst.

```
rm -f basic_auth.zip
zip basic_auth.zip main.py
aws --region us-east-1 s3 cp basic_auth.zip s3://your-bucket/
aws --region us-east-1 lambda update-function-code --s3-bucket your-bucket --s3-key basic_auth.zip --function-name your_func_name
aws --region us-east-1 lambda publish-version --function-name your_func_name
```

## Test

```
python3 -m unittest discover test
```

