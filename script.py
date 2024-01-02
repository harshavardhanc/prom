import ruamel.yaml

# Load the content of alert-values.yaml
with open('alert-values.yaml', 'r') as yaml_file:
    data = ruamel.yaml.YAML().load(yaml_file)

# Load the content of prom.rules
with open('prom.rules', 'r') as prom_rules_file:
    prom_rules_content = prom_rules_file.read()

# Append the prom.rules content under additionalPrometheusRules
data['prometheus']['additionalPrometheusRules'] = ruamel.yaml.scalarstring.PreservedScalarString(prom_rules_content)

# Write the updated content back to alert-values.yaml
with open('alert-values.yaml', 'w') as yaml_file:
    ruamel.yaml.YAML().dump(data, yaml_file)

print("Content appended successfully.")