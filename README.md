# datadog-max-file-age-check

Check directories do not contain files that are older than x

This check will report a gauge that contains the amount of files that are older than the specified max age

## Usage

Copy [the python file](./src/max_file_age_check.py) to `checks.d/max_file_age_check.py` then copy [the yaml file](./src/max_file_age_check.yaml) to `conf.d/max_file_age_check.yaml`

***Note: The name of the python file AND the yaml file [MUST be the same](https://docs.datadoghq.com/developers/write_agent_check/?tab=agentv6v7)***

### Configuration file

```yaml
instances:
  - path: "C:\\PathToMyFolder\\" # Path to folder
    max_age: 2 # Max age in minutes
    metric_name: custom.image_folder_expired_files # Name of metric in datadog
  - path: "C:\\PathToMySecondFolder\\"
    max_age: 2
    metric_name: custom.image_folder_two_expired_files
```
