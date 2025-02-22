import logging

import apscheduler.schedulers.background

import routers
import services

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("scheduler_logger")


def reset_daily_usage():
    routers.reset_gpt_usage()
    services.reset_image_search_usage()


scheduler = apscheduler.schedulers.background.BackgroundScheduler()

# 매일 17시(미국 서부 시간 기준 자정)마다 유료 모델과 이미지 검색 사용량 초기화
scheduler.add_job(reset_daily_usage, "cron", hour=17, minute=0)
scheduler.start()
