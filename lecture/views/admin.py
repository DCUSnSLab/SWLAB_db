from lecture.models import Lecture, LectureType
from lecture.serializers import CreateLectureSerializer, LectureAdminSerializer
from utils.api import APIView, validate_serializer
class BatchLecture(APIView):
    def post(self, request):
        print('test')
        # user = User.objects.create(username='test', email='test@test.com', schoolssn=12341234, realname='test')
        # user.set_password('12341234')
        # user.save()
        # print('user added')
        return self.success('??????')

class LectureAPI(APIView):
    @validate_serializer(CreateLectureSerializer)
    def post(self, request):
        print('lecture post')
        if request.user.is_admin_role():
            print('in Lecture is admin role')
            data = request.data
            data["lectype"] = LectureType.objects.get(id=data["lectype"])
            data["create_by"] = request.user
            print(data)
            lecture = Lecture.objects.create(**data)
            # signup_class.objects.create(lecture=lecture, user=request.user, status=False,
            #                             isallow=True)  # 수강 과목 생성 시, 본인이 생성한 수강과목에 대해 별도의 수강신청 없이 접근할 수 있도록
            # lecture_signup_class 테이블에 값을 생성한다.
            return self.success(LectureAdminSerializer(lecture).data)
        else:
            return self.success('Fail')

    # # def put(self, request):
    # @validate_serializer(EditLectureSerializer)
    # def put(self, request):
    #     data = request.data
    #     try:
    #         lecture = Lecture.objects.get(id=data.pop("id"))
    #         ensure_created_by(lecture, request.user)
    #     except Lecture.DoesNotExist:
    #         return self.error("no lecture exist")
    #
    #     for k, v in data.items():
    #         setattr(lecture, k, v)
    #     lecture.save()
    #     return self.success(LectureAdminSerializer(lecture).data)