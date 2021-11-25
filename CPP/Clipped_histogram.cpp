#include <opencv2/opencv.hpp>
#include <iostream>
using namespace cv;
using namespace std;
int NoOfBins = 65536;
int histogram[65536];
float therhold = 0.0001;
int NoOfPixel = 76800;
int new_total_number_pixel = 0;
#define max_value_hist NoOfPixel * therhold


int calculate_histogram(Mat image)
{
    int height = image.rows;
    int width  = image.cols;
    
    for (int i = 0; i < width; i++) {
        for (int j = 0; j < height; j++){
        histogram[image.at<u_int16_t>(i,j)] += 1; 
        }
    }
    return 0;
}

int cliped_histogram(void)
{
    for (int i = 0; i < NoOfBins; i++) 
    {
        if(max_value_hist < histogram[i])
        {
            histogram[i] = max_value_hist;        
        }
    }
    return 0;
}

int new_total_number_function()
{
    for (int i = 0; i < NoOfBins; i++) {
        new_total_number_pixel += histogram[i];
        }
    return 0;
}

int main(int argc, char** argv)
{
    float CDF[NoOfBins];
    float CDF_norm[NoOfBins];
    // Read the image file
    Mat image = imread("/home/kali/Documents/16BitFrames/frameIndex_500_2019-11-16_23.08.04.png", -1);

    // Check for failure
    if (image.empty())
    {
        cout << "Could not open or find the image" << endl;
        cin.get(); //wait for any key press
        return -1;
    }

    //equalize the histogram
    calculate_histogram(image);
    cliped_histogram();
    new_total_number_function();
    Mat proc_image = Mat::zeros(Size(image.cols,image.rows),CV_8UC1);

    for(int i = 0; i < NoOfBins; i++){
        CDF[i] = histogram[i] + CDF[i-1];
    }
    for(int i = 0; i < NoOfBins; i++){
        CDF_norm[i] = (CDF[i]/new_total_number_pixel)*255;
    }
    for(int y = 0; y < image.rows; y++){
        for(int x = 0; x < image.cols; x++)
        {
             proc_image.at<uchar>(y,x) = CDF_norm[image.at<u_int16_t>(y,x)];
        }
    }
                                               
    //Define names of windows
    String windowNameOfOriginalImage = "Original Image"; 
    String windowNameOfHistogramEqualized = "Histogram Equalized Image";

    // Create windows with the above names
    namedWindow(windowNameOfOriginalImage, WINDOW_NORMAL);
    namedWindow(windowNameOfHistogramEqualized, WINDOW_NORMAL);

    // Show images inside created windows.
    imshow(windowNameOfOriginalImage, image);
    imshow(windowNameOfHistogramEqualized, proc_image);

    waitKey(0); // Wait for any keystroke in one of the windows

    destroyAllWindows(); //Destroy all open windows

    return 0;
}