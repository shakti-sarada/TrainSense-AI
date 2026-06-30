from pathlib import Path

ROOT = Path(".")

directories = [
    "api",
    "agents",
    "agents/prompts",
    "services",
    "ml",
    "ml/models",
    "background",
    "integrations",
    "integrations/data",
    "db",
    "db/migrations",
    "db/seed",
    "guardrails",
    "core",
    "tests",
    "tests/test_services",
    "tests/test_agents",
    "tests/test_ml",
    "tests/test_integrations",
]

files = [
    # Root files
    "main.py",
    "Dockerfile",
    "requirements.txt",
    ".env.example",

    # ---------------- API ----------------
    "api/__init__.py",
    "api/chat.py",
    "api/clear.py",
    "api/subscribe.py",
    "api/health.py",
    "api/preferences.py",
    "api/metrics.py",

    # ---------------- Agents ----------------
    "agents/__init__.py",
    "agents/graph.py",
    "agents/orchestrator_agent.py",
    "agents/constraint_extraction_agent.py",
    "agents/conversation_memory_agent.py",
    "agents/explainable_recommendation_agent.py",

    # Agent Prompts
    "agents/prompts/__init__.py",
    "agents/prompts/constraint_extraction_prompt.py",
    "agents/prompts/orchestrator_prompt.py",
    "agents/prompts/conversation_memory_prompt.py",
    "agents/prompts/explanation_prompt.py",

    # ---------------- Services ----------------
    "services/__init__.py",
    "services/cache_service.py",
    "services/health_monitor_service.py",
    "services/api_fallback_manager.py",
    "services/circuit_breaker.py",
    "services/seat_warning_engine.py",
    "services/alternate_boarding_service.py",
    "services/via_route_service.py",
    "services/nearby_station_service.py",
    "services/flexible_date_scanner.py",
    "services/ranking_service.py",
    "services/explanation_input_builder.py",
    "services/preferences_store.py",
    "services/observability_service.py",

    # ---------------- ML ----------------
    "ml/__init__.py",
    "ml/wl_confirmation_model.py",
    "ml/delay_prediction_model.py",
    "ml/train_wl_model.py",
    "ml/train_delay_model.py",

    # Placeholder model files
    "ml/models/wl_confirmation.pkl",
    "ml/models/delay_prediction.pkl",

    # ---------------- Background ----------------
    "background/__init__.py",
    "background/notification_scheduler.py",

    # ---------------- Integrations ----------------
    "integrations/__init__.py",
    "integrations/erail_client.py",
    "integrations/indianrailapi_client.py",
    "integrations/ntes_scraper.py",
    "integrations/station_mapper.py",
    "integrations/data/stations.json",

    # ---------------- Database ----------------
    "db/__init__.py",
    "db/connection.py",
    "db/models.py",

    # Migrations
    "db/migrations/001_train_cache.sql",
    "db/migrations/002_user_preferences.sql",
    "db/migrations/003_subscriptions.sql",
    "db/migrations/004_wl_trends.sql",
    "db/migrations/005_historical_delays.sql",
    "db/migrations/006_sessions.sql",
    "db/migrations/007_request_metrics.sql",
    "db/migrations/008_api_health.sql",

    # Seed scripts
    "db/seed/seed_wl_trends.py",
    "db/seed/seed_historical_delays.py",

    # ---------------- Guardrails ----------------
    "guardrails/__init__.py",
    "guardrails/input_guardrails.py",
    "guardrails/output_guardrails.py",
    "guardrails/rate_limiter.py",

    # ---------------- Core ----------------
    "core/__init__.py",
    "core/config.py",
    "core/session_memory.py",
    "core/constants.py",
    "core/booking_constraints.py",
    "core/hitl.py",

    # ---------------- Tests ----------------
    "tests/__init__.py",
]

print("\nCreating TrainSense AI backend structure...\n")

# Create directories
for directory in directories:
    path = ROOT / directory
    path.mkdir(parents=True, exist_ok=True)
    print(f"[DIR ] {path}")

# Create files
for file in files:
    path = ROOT / file
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.touch()
        print(f"[FILE] {path}")
    else:
        print(f"[SKIP] {path}")

print("\n" + "=" * 60)
print("✅ TrainSense AI backend structure created successfully!")
print("=" * 60)