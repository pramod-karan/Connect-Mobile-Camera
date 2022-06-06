import cv2

#IPV4 address
ipv4_url = 'http://192.168.43.28:8080'

#Read Video
cam = f'{ipv4_url}/video'
cap = cv2.VideoCapture(cam)

while True:
	#read each frame from video
	ret, frame = cap.read()
	#resize Frame
	frame = cv2.resize(frame, (600,600))
	#display frame
	cv2.imshow("Mobile camera", frame)
	#press q to break the loop
	if cv2.waitKey(1) == ord('q'):
		break

#release Camer
cap.release()
#distroy windows
cv2.destroyAllWindows()

