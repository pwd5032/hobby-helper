
$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Content-Type", "application/json")

$data = @{
    "name" = "My Bean"
    "roast" = "Medium"
    "origin" = "Colombia"
    "notes" = "Tastes like chocolate"
    "purchase_location" = "Online"
    "purchase_date" = "2022-05-01"
    "roast_date" = "2022-05-02"
    "freeze_date" = "2022-05-03"
    "first_unfreeze_date" = "2022-05-05"
    "second_unfreeze_date" = "2022-05-07"
} | ConvertTo-Json

Invoke-WebRequest -Method Post -Uri 'http://localhost:8000/api/beans/add/' -Headers $headers -Body $data


