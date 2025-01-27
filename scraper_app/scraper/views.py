from django.shortcuts import render
from django.http import JsonResponse
from .models import Task, ScrapedData

def simulate_scraping(task):
    if task.scenario == 'social-media':
        return [{"name": "User1", "email": "user1@social.com"}, {"name": "User2", "email": "user2@social.com"}]
    elif task.scenario == 'find-person':
        return [{"name": "John Doe", "position": "Manager", "company": task.input_data['company_name'], "email": "john@example.com"}]
    elif task.scenario == 'job-search':
        return [{"name": None, "position": "Developer", "company": "Tech Corp", "email": None}]
    elif task.scenario == 'data-enrichment':
        return [{"name": "Alice Smith", "position": "CEO", "company": task.input_data['company_name'], "email": "alice@example.com"}]
    elif task.scenario == 'database-search':
        return [{"name": "Bob Johnson", "position": "CTO", "company": "Innovate Inc", "email": "bob@example.com"}]
    return []

def home(request):
    return render(request, 'scraper/home.html')

def create_task(request):
    if request.method == 'POST':
        scenario = request.POST.get('scenario')
        input_data = {
            key: request.POST[key] for key in request.POST if key != 'scenario'
        }
        
        if scenario == 'find-person' and 'company_name' not in input_data:
            return JsonResponse({"status": "error", "message": "Company name is required for 'Find Person' scenario."}, status=400)

        task = Task.objects.create(scenario=scenario, input_data=input_data)
        scraped_data = simulate_scraping(task)
        for data in scraped_data:
            ScrapedData.objects.create(task=task, **data)
        return JsonResponse({"status": "success", "task_id": task.id})
    
def fetch_data(request, task_id):
    scraped_data = ScrapedData.objects.filter(task_id=task_id).values()
    return JsonResponse(list(scraped_data), safe=False)



