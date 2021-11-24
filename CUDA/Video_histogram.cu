__global__ void convolve(unsigned char *source, int width, int height, int paddingX, int paddingY, ssize_t kOffset, int kWidth, int kHeight, unsigned char *destination)
{
    // Calculate our pixel's location
    int x = (blockIdx.x * blockDim.x) + threadIdx.x;
    int y = (blockIdx.y * blockDim.y) + threadIdx.y;

    float sum = 0.0;
    int   pWidth = kWidth/2;
    int   pHeight = kHeight/2;

    // Only execute for valid pixels
    if(x >= pWidth+paddingX &&
       y >= pHeight+paddingY &&
       x < (blockDim.x * gridDim.x)-pWidth-paddingX &&
       y < (blockDim.y * gridDim.y)-pHeight-paddingY)
    {
        for(int j = -pHeight; j <= pHeight; j++)
        {
            for(int i = -pWidth; i <= pWidth; i++)
            {
                // Sample the weight for this location
                int ki = (i+pWidth);
                int kj = (j+pHeight);
                float w  = convolutionKernelStore[(kj * kWidth) + ki + kOffset];

        
                sum += w * float(source[((y+j) * width) + (x+i)]);
            }
        }
    }
    