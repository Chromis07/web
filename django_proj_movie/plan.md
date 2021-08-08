프로젝트 : django_proj_movie

주요 모델

- Actor : 주연배우
    name
    photo : image
- Movie : Actor와 1:N
    name
    poster : image
    desc : text
- Video : 프로모션 유튜브 비디오, Movie와 1:N
    name
    youtube_url : models.URLField()
- Review : Movie와 1:N

admin을 활용한 Actor/Movie/PromotionVideo 관리
유저에게
 - Actor List (이미지 노출)
 - Actor Detail : + 출연영화 목록 (포스터 이미지)
 - Movie List (포스터 이미지)
 - Movie Detail : + 프로모션 유튜브 비디오 목록 + 리뷰 목록/쓰기/수정/삭제
     - Video URL 목록을 보여줄 수도 있고.
         - 욕심을 낸다면 ... youtube video embed