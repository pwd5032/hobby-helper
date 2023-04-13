$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Content-Type", "application/json")

$data = @{
    grind_size = 20
    brew_time = "00:03:30"
    yield_ratio = 2.5
    beans_fk = 1
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/brews/add/" -Method POST -Headers $headers -Body $data
